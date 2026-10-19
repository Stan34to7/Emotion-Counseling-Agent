(function () {
  "use strict";

  const SESSION =
    (window.localStorage && localStorage.getItem("cx_session_id")) ||
    "User";
  const API_BASE = "/clinical-expert";
  const POLL_MS = 2500;
  const COLLAPSE_KEY = "cx_panel_collapsed";

  function esc(s) {
    return String(s ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function tone(statusKey) {
    if (["candidate", "weak_support", "supported"].includes(statusKey)) return "cx-st-up";
    if (["insufficient", "weakened", "ruled_out"].includes(statusKey)) return "cx-st-down";
    return "";
  }

  function isCollapsed() {
    try {
      return localStorage.getItem(COLLAPSE_KEY) === "1";
    } catch {
      return false;
    }
  }

  function setCollapsed(on) {
    document.body.classList.toggle("cx-panel-collapsed", !!on);
    try {
      localStorage.setItem(COLLAPSE_KEY, on ? "1" : "0");
    } catch {
      /* ignore */
    }
    const btn = document.getElementById("cx-toggle");
    if (btn) {
      btn.setAttribute("aria-expanded", on ? "false" : "true");
      btn.title = on ? "展开状态栏" : "折叠状态栏";
      btn.textContent = on ? "状态" : "收起";
    }
  }

  function ensureDom() {
    document.body.classList.add("cx-clinical");
    const right = document.querySelector(".main_right");
    if (!right || document.getElementById("cx-panel")) return;

    // Do NOT move Vue-managed nodes (breaks chat rendering).
    const panel = document.createElement("aside");
    panel.id = "cx-panel";
    panel.setAttribute("aria-label", "临床状态");
    panel.innerHTML = `
      <div class="cx-head">
        <div class="cx-head-text">
          <h2>状态</h2>
          <p class="cx-sub">根据对话更新，不是结论</p>
        </div>
        <div class="cx-head-actions">
          <span class="cx-badge" id="cx-badge">心理专家</span>
          <button type="button" class="cx-toggle" id="cx-toggle" aria-expanded="true">收起</button>
        </div>
      </div>
      <div class="cx-panel-main" id="cx-panel-main">
        <details class="cx-trace" open>
          <summary>本轮在想什么</summary>
          <ol class="cx-process" id="cx-process"></ol>
        </details>
        <div class="cx-body" id="cx-body">
          <p class="cx-muted">开始对话后，这里会记下此刻状态、可能方向、还想了解的事，以及原话证据。</p>
        </div>
        <div class="cx-foot">研究原型 · 不下诊断 · 紧急情况请寻求现场帮助</div>
      </div>
    `;
    right.appendChild(panel);

    const toggle = document.getElementById("cx-toggle");
    if (toggle) {
      toggle.addEventListener("click", function () {
        setCollapsed(!document.body.classList.contains("cx-panel-collapsed"));
      });
    }
    setCollapsed(isCollapsed());
  }

  function render(payload) {
    const body = document.getElementById("cx-body");
    const process = document.getElementById("cx-process");
    const badge = document.getElementById("cx-badge");
    if (!body || !process) return;

    const expert = (payload && payload.expert) || {};
    const llm = (payload && payload.llm) || {};
    if (badge) {
      badge.textContent = llm.used ? `本地 ${llm.model || "Qwen"}` : "心理专家";
    }

    const steps = expert.process_steps || [];
    process.innerHTML = steps.length
      ? steps
          .map(
            (s, i) => `<li class="cx-step">
          <div class="t">${esc(s.title || "步骤 " + (i + 1))}</div>
          <div class="s">${esc(s.summary || "")}</div>
          ${
            (s.items || []).length
              ? `<ul>${(s.items || []).slice(0, 4).map((x) => `<li>${esc(x)}</li>`).join("")}</ul>`
              : ""
          }
        </li>`
          )
          .join("")
      : `<li class="cx-muted" style="list-style:none;padding:8px 0">等待本轮分析…</li>`;

    const observed = expert.observed || [];
    const hyps = expert.active_hypotheses || [];
    const missing = expert.missing_information || [];
    const evidence = expert.evidence || [];
    const spt = expert.state_pattern_trait || {};
    const why = expert.why_this_question || "";

    if (!observed.length && !evidence.length && !hyps.length && !missing.length) {
      body.innerHTML = `<p class="cx-muted">开始对话后，这里会记下你的状态、可能方向，以及还想了解的事。</p>`;
      return;
    }

    const chips = (arr, cls) =>
      (arr || [])
        .slice(0, 10)
        .map((x) => {
          const label = typeof x === "string" ? x : x.name || x.label || JSON.stringify(x);
          return `<span class="cx-chip ${cls || ""}">${esc(label)}</span>`;
        })
        .join("") || `<span class="cx-muted">—</span>`;

    const hypHtml = hyps.length
      ? hyps
          .slice(0, 8)
          .map((h) => {
            const name = h.name || h.target || h.label || "假设";
            const st = h.status || h.status_key || "";
            return `<div class="cx-hyp"><div class="top"><span>${esc(name)}</span><span class="${tone(
              h.status_key || ""
            )}">${esc(st)}</span></div></div>`;
          })
          .join("")
      : `<p class="cx-muted">还在听。</p>`;

    const evHtml = evidence.length
      ? evidence
          .slice()
          .reverse()
          .slice(0, 8)
          .map((e) => {
            const utt = e.utterance || e.text || "";
            const tid = e.turn_id || "";
            return `<div class="cx-ev"><span class="cx-tid">${esc(tid)}</span>${esc(utt)}</div>`;
          })
          .join("")
      : `<p class="cx-muted">—</p>`;

    body.innerHTML = `
      <div class="cx-block"><h3>此刻状态</h3><div class="cx-chips">${chips(observed)}</div></div>
      <div class="cx-block"><h3>可能方向</h3><p class="cx-note">多种可能同时保留，不会锁死。</p>${hypHtml}</div>
      <div class="cx-block"><h3>还想了解</h3><div class="cx-chips">${chips(missing, "miss")}</div></div>
      <div class="cx-block"><h3>下一问意图</h3><p class="cx-note">${esc(why || "—")}</p></div>
      <div class="cx-block"><h3>原话</h3>${evHtml}</div>
      <div class="cx-block"><h3>累积</h3>
        <p class="cx-note">${esc(spt.note || "一句话只是线索，重复出现才会记成模式。")}</p>
      </div>
    `;
  }

  async function pull() {
    try {
      const r = await fetch(`${API_BASE}/v1/expert/panel?session_id=${encodeURIComponent(SESSION)}`, {
        cache: "no-store",
      });
      if (!r.ok) return;
      const data = await r.json();
      if (data && data.ok) render(data);
    } catch {
      /* ignore transient */
    }
  }

  function boot() {
    ensureDom();
    pull();
    setInterval(pull, POLL_MS);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
