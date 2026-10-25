import ast
import copy
import os
from pathlib import Path
import shutil
import sys
import tempfile
import datetime
import json
import re
import requests
import textwrap
import types
import unittest
from typing import Any, Dict, List, Optional
from unittest.mock import Mock, patch

import numpy as np
import yaml

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from llm.knowledge_cards import (
    KnowledgeCardStore, KnowledgeUnavailable, PROJECT_ROOT,
    RISK_REFERRAL, format_card_context, retrieve_card_context,
)


class ConstantEmbedder:
    def __init__(self):
        self.builds = 0

    def passage_embed(self, documents):
        self.builds += 1
        return [np.array([1, 0, 0]) for _ in documents]

    def query_embed(self, query):
        return [np.array([1, 0, 0])]


def load_functions(path, names, namespace):
    """Execute actual functions without importing app startup, databases, or audio hardware."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    nodes = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(path), "exec"), namespace)


class CardFixture:
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("knowledge-cards", "professional-sources"):
            shutil.copytree(PROJECT_ROOT / "rag" / directory, self.root / directory)
        self.embedder = ConstantEmbedder()
        self.store = KnowledgeCardStore(self.root, embedder=self.embedder)

    def update_card(self, card_id, **fields):
        path = self.root / "knowledge-cards" / "provisional-runtime" / f"{card_id}.yaml"
        card = yaml.safe_load(path.read_text(encoding="utf-8"))
        card.update(fields)
        path.write_text(yaml.safe_dump(card, allow_unicode=True), encoding="utf-8")


class CardStoreTests(CardFixture, unittest.TestCase):
    def test_loads_only_originals_and_deduplicates_vector_hits(self):
        (self.root / "全文").mkdir()
        (self.root / "全文" / "duplicate.md").write_text("DUPLICATE", encoding="utf-8")
        self.assertEqual(self.store.status()["card_count"], 18)
        hits = self.store.search("示例", top_k=10)
        self.assertEqual(len(hits), 10)
        self.assertEqual(len({hit["id"] for hit in hits}), 10)
        self.assertTrue(all("sources" in hit and "matched_text" in hit for hit in hits))
        self.assertEqual(self.store.status()["index_backend"], "faiss")

    def test_permissions_and_verification_are_enforced(self):
        self.update_card("DEP_MOOD_001", runtime_permission="RESEARCH_ONLY")
        self.update_card("ANX_ASSESS_001", verification={"source_verified": False, "structure_verified": True})
        self.update_card("BIP_SLEEP_001", runtime_permission="PRODUCTION_RUNTIME")
        self.assertEqual(self.store.status()["card_count"], 15)

    def test_unknown_source_is_not_silently_used(self):
        self.update_card("DEP_MOOD_001", sources=[{"source_id": "missing", "locator": "1"}])
        with self.assertRaises(KnowledgeUnavailable):
            self.store.search("难过")
        self.assertFalse(self.store.status()["corpus_loaded"])

    def test_duplicate_id_is_rejected(self):
        self.update_card("DEP_MOOD_001", id="ANX_ASSESS_001")
        with self.assertRaises(KnowledgeUnavailable):
            self.store.search("难过")

    def test_caches_index_and_reloads_changed_card(self):
        self.store.search("示例")
        self.store.search("示例")
        self.assertEqual(self.embedder.builds, 1)
        self.update_card("DEP_MOOD_001", retrieval_text_zh="更新后的检索描述")
        self.store.search("示例")
        self.assertEqual(self.embedder.builds, 2)

    def test_results_cannot_mutate_shared_corpus(self):
        first = self.store.search("示例", top_k=1)
        original = copy.deepcopy(first)
        first[0]["sources"][0]["source_id"] = "changed"
        self.assertEqual(self.store.search("示例", top_k=1), original)

    def test_invalid_top_k_and_empty_query(self):
        for value in (0, -1, 11, True, "3", 1.2):
            with self.subTest(value=value), self.assertRaises(ValueError):
                self.store.search("示例", value)
        self.assertEqual(self.store.search(" "), [])

    def test_invalid_embeddings_fail_and_chat_degrades(self):
        self.embedder.passage_embed = lambda docs: [np.zeros(3) for _ in docs]
        with self.assertRaises(KnowledgeUnavailable):
            self.store.search("难过")
        with patch("llm.knowledge_cards.get_card_store", return_value=self.store):
            self.assertEqual(retrieve_card_context("难过"), ("", []))

    def test_boundaries_and_risk_template_reach_prompt(self):
        self.store._read_corpus()
        risk = next(card for card in self.store._cards if card["id"] == "SH_RISK_001")
        context = format_card_context([risk])
        self.assertIn("SH_RISK_001", context)
        self.assertIn("future_suicide_probability_score", context)
        self.assertIn("PROVISIONAL_RUNTIME", context)
        self.assertIn("nice-ng225", context)
        self.assertIn(RISK_REFERRAL, context)


class KnowledgeApiTests(CardFixture, unittest.TestCase):
    # These tests mount the production handlers in an isolated Flask app.
    def setUp(self):
        super().setUp()
        from flask import Flask, jsonify, request

        self.app = Flask(__name__)
        namespace = {"__app": self.app, "request": request, "jsonify": jsonify}
        load_functions(BACKEND / "gui" / "flask_server.py", {"api_knowledge_search", "api_knowledge_status"}, namespace)
        self.client = self.app.test_client()
        self.patcher = patch("llm.knowledge_cards.get_card_store", return_value=self.store)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_api_returns_traceable_cards(self):
        response = self.client.post("/api/knowledge/search", json={"query": "难过", "top_k": 2})
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertEqual(payload["count"], 2)
        self.assertTrue(payload["retrieval"]["semantic_ready"])
        self.assertIn("locator", payload["cards"][0]["sources"][0])

    def test_api_validates_body_and_limits(self):
        for data in ([], {}, {"query": 5}, {"query": "x", "top_k": True}, {"query": "x" * 2001}):
            with self.subTest(data_type=type(data).__name__):
                self.assertEqual(self.client.post("/api/knowledge/search", json=data).status_code, 400)

    def test_status_does_not_download_model(self):
        response = self.client.get("/api/knowledge/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["card_count"], 18)
        self.assertFalse(response.get_json()["semantic_ready"])
        self.assertEqual(self.embedder.builds, 0)

    def test_api_returns_503_if_retrieval_unavailable(self):
        self.store.root = self.root / "missing"
        response = self.client.post("/api/knowledge/search", json={"query": "难过"})
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.get_json()["cards"], [])


class ChatInjectionTests(unittest.TestCase):
    def test_main_streaming_chat_uses_cards_instead_of_expert_shortcut(self):
        from langchain_core.messages import HumanMessage, SystemMessage

        captured = []
        stream = Mock()
        stream.get_conversation_id.return_value = "test-conversation"
        stream.should_stop_generation.return_value = False
        database = Mock()
        database.get_recent_messages_by_user.return_value = []
        member = Mock()
        member.get_current_model.return_value = None
        core = types.ModuleType("core")
        core.stream_manager = types.SimpleNamespace(new_instance=lambda: stream)
        core.member_db = types.SimpleNamespace(new_instance=lambda: member)

        def stream_reply(messages):
            captured.append(messages)
            return [types.SimpleNamespace(content="测试回复。")]

        retrieve = Mock(return_value=("DEP_MOOD_001: does_not_establish=depressive_disorder", [{"id": "DEP_MOOD_001"}]))
        namespace = {
            "Any": Any, "List": List, "Dict": Dict, "Optional": Optional,
            "WorkflowToolSpec": object, "ConversationMessage": dict, "AgentState": dict,
            "SystemMessage": SystemMessage, "HumanMessage": HumanMessage,
            "datetime": datetime, "json": json, "re": re, "textwrap": textwrap, "requests": requests,
            "agents": {}, "current_username": None,
            "cfg": types.SimpleNamespace(load_config=lambda: None, config={"attribute": {}}),
            "util": types.SimpleNamespace(log=lambda *args: None),
            "content_db": types.SimpleNamespace(new_instance=lambda: database),
            "create_agent": lambda *args: types.SimpleNamespace(scratch={}, memory_stream=None),
            "get_knowledge_base": lambda: {}, "retrieve_card_context": retrieve,
            "SOULLINK_THERAPY_SUFFIX": "therapy",
            "_build_emotion_policy_suffix": lambda _: "",
            "_should_skip_workflow_for_request": lambda *args: True,
            "_get_builtin_tool_specs": lambda: {}, "get_mcp_tools": lambda: [],
            "_truncate_history": lambda _: "", "llm": types.SimpleNamespace(stream=stream_reply),
            "MyThread": Mock(), "remember_conversation_thread": Mock(),
        }
        load_functions(BACKEND / "llm" / "nlp_cognitive_stream.py", {"question", "_build_final_messages"}, namespace)
        with patch.dict(sys.modules, {"core": core, "utils.stream_state_manager": None, "utils.stream_text_processor": None}), patch(
            "llm.soullink_expert_hook.call_expert_turn", return_value={"ok": True, "spoken_text": "EXPERT"}
        ) as expert:
            self.assertEqual(namespace["question"]("最近心情低落", "test"), "测试回复。")
            self.assertTrue(any("DEP_MOOD_001" in message.content for message in captured[0]))
            expert.assert_not_called()
            namespace["question"]("最近心情低落", "test", pure_mode=True)
            self.assertEqual(retrieve.call_count, 1)
            self.assertFalse(any("DEP_MOOD_001" in message.content for message in captured[1]))

    def test_direct_chat_receives_card_boundaries_and_can_disable_rag(self):
        from langchain_core.messages import SystemMessage

        captured = []

        class FakeLlm:
            def __init__(self, **kwargs):
                pass

            def invoke(self, messages):
                captured.append(messages)
                return types.SimpleNamespace(content="测试回复")

        namespace = {
            "Optional": Optional,
            "cfg": types.SimpleNamespace(load_config=lambda: None, gpt_base_url="http://unused",
                                         key_gpt_api_key="test", gpt_model_engine="test"),
            "util": types.SimpleNamespace(log=lambda *args: None),
        }
        load_functions(BACKEND / "llm" / "llm_service.py", {"chat_with_model"}, namespace)
        with patch("langchain_openai.ChatOpenAI", FakeLlm), patch(
            "llm.knowledge_cards.retrieve_card_context", return_value=("DEP_MOOD_001: does_not_establish=depressive_disorder", [{"id": "DEP_MOOD_001"}])
        ) as retrieve:
            namespace["chat_with_model"]("最近伤心", "test", history=[{"role": "user", "content": "你好"}])
            self.assertTrue(any(isinstance(message, SystemMessage) and "DEP_MOOD_001" in message.content for message in captured[0]))
            namespace["chat_with_model"]("最近伤心", "test", use_knowledge_cards=False)
            self.assertEqual(retrieve.call_count, 1)
            self.assertFalse(any("DEP_MOOD_001" in message.content for message in captured[1]))


@unittest.skipUnless(os.getenv("SOULLINK_TEST_SEMANTIC") == "1", "Enable real cached BGE inference with SOULLINK_TEST_SEMANTIC=1")
class SemanticRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.store = KnowledgeCardStore()

    def test_chinese_scenarios_retrieve_expected_card_first(self):
        scenarios = {
            "上课时脑子总飘到别处，做题也集中不了，是不是多动症": "ADHD_CONC_001",
            "网上的多动症测评给我打了高分，这样就能确诊吗": "ADHD_DX_001",
            "只有在学校分心，回家却很专注，这说明什么": "ADHD_DX_002",
            "以前爱打游戏，现在懒得打开，但写程序还很投入": "ANHED_SCOPE_001",
            "还没考试就一直害怕考砸，心跳快，夜里翻来覆去": "ANX_ASSESS_001",
            "有时异常兴奋话很多，后来又低落，该了解哪些情况": "BIP_ASSESS_001",
            "只睡了三小时也一点不累，整天停不下来": "BIP_SLEEP_001",
            "这周经常熬夜，睡眠短就是轻躁狂吗": "BIP_SLEEP_002",
            "连着几个星期没精神，对什么都提不起劲，该怎么了解": "DEP_ASSESS_001",
            "今天心里特别难受一直想哭，是抑郁症吗": "DEP_MOOD_001",
            "能通过我说的话给我一个大五人格百分位吗": "PERS_IPIP_001",
            "最近有些奇怪的感知经历，评估时该看哪些方面": "PSY_ASSESS_001",
            "总觉得同事暗中盯着我，就能认定是妄想吗": "PSY_BELIEF_001",
            "RDoC 能用来直接给人做 ICD 诊断吗": "RDOC_LIM_001",
            "我想伤害自己，活着太痛苦了": "SH_RISK_001",
            "能把自杀的可能性分成低中高来决定能不能出院吗": "SH_RISK_002",
            "这阵子总躲着朋友，不想参加聚会，是人格障碍吗": "SOC_TRAIT_001",
            "我今天发火了，是不是说明我性格一直很坏": "STATE_TRAIT_001",
        }
        for query, expected in scenarios.items():
            with self.subTest(card=expected):
                hits = self.store.search(query)
                self.assertTrue(hits)
                self.assertEqual(hits[0]["id"], expected)
                self.assertTrue(hits[0]["sources"][0]["url"].startswith("https://"))

    def test_unrelated_and_positive_inputs_do_not_force_a_card(self):
        for query in ("你好", "帮我查北京天气", "写个冒泡排序", "今晚上吃什么", "我很开心，今天考试通过了", "我写代码时很专注"):
            with self.subTest(query=query):
                self.assertEqual(self.store.search(query), [])


if __name__ == "__main__":
    unittest.main()
