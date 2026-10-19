# SoulLink

一个面向虚拟陪伴、数字人对话与 3D 角色驱动场景的多模块项目。  
项目将 Python 后端、语音能力、LLM、多角色管理、MCP 工具调用、3D 模型生成/绑骨/动作驱动，以及 React 前端整合到了一套完整工程中。

## 项目概览

SoulLink 不是单一网页，而是由以下几部分协同组成：

- Python 主后端：负责配置加载、对话编排、数据库、ASR、TTS、WebSocket、MCP 服务等
- Flask 管理后台：提供系统管理、模型管理、接口代理、健康检查等能力
- `soullink/` 前端：提供首页智能体、角色创建、3D 绑定、互动聊天、系统管理等页面
- `mesh2motion/` 子项目：提供动作重定向与 3D 模型处理能力
- `mcp_servers/`：提供可接入 Fay 的 MCP 服务示例

适用场景包括：

- AI 虚拟陪伴
- 多角色数字人对话
- 语音驱动的虚拟角色交互
- 3D 角色生成与展示
- 角色长期记忆与个性化互动
- Android 虚拟陪伴应用原型

## 核心能力

- 文本对话与语音对话
- 支持 ASR / LLM / TTS 多模块组合
- WebSocket 实时文本、状态与音频协同
- 角色属性生成、角色切换、角色管理
- 3D 模型上传、文生 3D、图生 3D
- 自动绑骨与动作模型管理
- 长期记忆与本地持久化
- MCP 工具注册与调用
- Web 端、桌面模式、Android 封装

## 技术栈

### 后端

- Python 3.12
- Flask
- gevent
- WebSocket / websocket-client / ws4py
- PyQt5
- SQLite
- LangChain
- LangGraph
- MCP

### AI / 多模态

- ASR：阿里云语音识别、FunASR
- TTS：阿里云、微软、火山、GPT-SoVITS
- LLM：OpenAI 兼容接口、DashScope 兼容接口
- 情绪分析：百度情感分析等
- 3D 生成：Hunyuan3D
- 自动绑骨：Make It Animatable

### 前端

- React 19
- TypeScript
- Vite
- Tailwind CSS
- Three.js
- React Router
- Capacitor Android

## 系统结构

### 运行入口

- `main.py`：项目主入口，启动数据库、Flask、WebSocket、MCP 等服务
- `fay_booter.py`：数字人核心对象启动与停止
- `gui/flask_server.py`：管理后台、API、模型管理、Hunyuan3D 代理等
- `core/fay_core.py`：对话主链路
- `soullink/`：React + Three.js 前端

### 目录说明

```text
.
├─ main.py                     # 后端主入口
├─ fay_booter.py               # 数字人核心启动器
├─ requirements.txt            # Python 依赖
├─ system.conf                 # 系统级配置
├─ config.json                 # 角色与交互配置
├─ core/                       # 交互、数据库、录音、WebSocket 等核心逻辑
├─ gui/                        # Flask 管理后台与页面资源
├─ llm/                        # LLM 与认知链路
├─ asr/                        # 语音识别模块
├─ tts/                        # 语音合成模块
├─ ai_module/                  # 情绪识别等 AI 模块
├─ faymcp/                     # MCP 管理服务与页面
├─ mcp_servers/                # MCP 服务示例
├─ memory/                     # 记忆数据与 SQLite 数据库
├─ models/                     # 角色 3D 模型与动作资源
├─ soullink/                   # React 前端与 Android 封装工程
├─ mesh2motion/                # 动作重定向子项目
├─ docs/                       # 架构与集成说明
├─ logs/                       # 运行日志
└─ test/                       # 测试与实验脚本
```

## 运行环境

推荐环境：

- Python 3.12
- Node.js 18+
- npm 9+
- Windows 10/11、macOS、Ubuntu

如果在 Linux 上启用音频相关能力，建议先安装：

```bash
sudo apt update
sudo apt install build-essential portaudio19-dev ffmpeg
```

## 快速开始

### 1. 安装后端依赖

```bash
pip install -r requirements.txt
```

### 2. 检查配置文件

项目启动前至少要检查这两个文件：

- `system.conf`
- `config.json`

重点配置项如下：

#### `system.conf`

- `start_mode`：启动模式，常见为 `web` 或 `common`
- `ASR_mode`：语音识别模块，如 `ali`
- `tts_module`：语音合成模块，如 `ali`
- `gpt_base_url`：LLM 服务地址
- `gpt_api_key`：LLM 密钥
- `gpt_model_engine`：模型名称
- `fay_url`：对外访问地址，常用于代理或移动端访问

#### `config.json`

- `attribute`：默认角色属性
- `interact`：交互逻辑、Q&A、播放音效等
- `make_it_animatable_api_url`：自动绑骨服务地址
- `memory.isolate_by_user`：是否按用户隔离记忆
- `source.wake_word`：唤醒词配置

### 3. 启动后端

只启动基础服务：

```bash
python main.py
```

启动基础服务并自动拉起数字人主服务：

```bash
python main.py start
```

说明：

- `python main.py` 会启动 Flask、WebSocket、MCP 等服务
- `python main.py start` 会在此基础上自动启动数字人核心
- 运行后也可以在控制台输入 `start`、`stop`、`restart`、`help`

### 4. 访问管理后台

后端默认入口：

- 管理后台：`http://127.0.0.1:5002/`
- 健康检查：`http://127.0.0.1:5002/health`

如果你前面有 Nginx 反向代理，也可能通过 `5000` 或你配置的域名访问。

## 前端子项目 `soullink/`

`soullink/` 是独立的 React 前端，负责：

- 首页智能体引导
- 角色创建
- 3D 模型预览
- 绑定与动作处理
- 3D 聊天互动
- 系统管理
- Android 打包

### 安装依赖

```bash
cd soullink
npm install
```

### 开发启动

```bash
npm run dev
```

默认端口：

- Vite：`5173`

### 推荐开发配置

在 `soullink/.env.local` 中配置：

```env
VITE_FAY_API_URL=http://127.0.0.1:5002
VITE_DEV_BACKEND=http://127.0.0.1:5002
```

说明：

- 前端默认会把 `/api` 代理到 `VITE_DEV_BACKEND` 或 `VITE_FAY_API_URL`
- 如果你实际通过 Nginx 暴露的是 `5000` 或域名，请把这里改成和真实入口一致
- 移动端不要使用 `127.0.0.1`，应改成电脑局域网 IP 或公网域名

### 构建

```bash
npm run build
```

### Android 打包

```bash
npm run android:build
```

打开 Android 工程：

```bash
npm run android:open
```

更多说明可参考：

- `soullink/DEPLOY_ANDROID.md`
- `soullink/DOMAIN_CONFIG_GUIDE.md`

## 使用手册

### 1. 首页智能体

对应页面：`/`

主要能力：

- 直接通过自然语言描述需求
- 上传参考图片创建角色
- 上传 3D 模型继续处理
- 让系统自动判断是“聊天”、“建角色”还是“去绑定/互动”

常见用法：

- “我想和孔子对话”
- “帮我创建一个温柔的虚拟伙伴”
- “我想和这张图里的角色聊天”
- “帮我绑定并和这个角色对话”

### 2. 创建页

对应页面：`/create`

适合手动完成角色创建流程，支持：

- 文生 3D
- 图生 3D
- 角色属性生成
- 3D 模型预览
- 创建后保存到后端模型库

### 3. 绑定页

对应页面：`/bind`

主要功能：

- 对当前角色进行自动绑骨
- 使用 Mesh2Motion 处理动作
- 生成 `idle` / `talking` / `wave` 等动作模型
- 完成后进入聊天互动页

如果自动绑骨失败，也可以在这里继续手动处理。

### 4. 聊天互动页

对应页面：`/chat`

主要能力：

- 3D 角色展示
- 文本输入与语音输入
- WebSocket 实时推送
- 音频播放与动作切换
- 背景切换
- 清空当前对话

说明：

- 若角色已有 `idleModelUrl`、`talkingModelUrl`、`waveModelUrl`，会优先使用动作模型
- 若没有动作模型，会回退到基础 `model3dUrl`

### 5. 管理页

对应页面：`/manage`

主要功能：

- 查看和切换角色
- 上传/配置 3D 模型
- 上传/配置动画模型
- 配置后端 API 地址
- 查看情绪趋势报告
- 删除角色

移动端或多设备联调时，优先在这里检查 API 地址是否正确。

## 后端接口概览

项目中较常用的接口包括：

- `GET /health`：健康检查
- `POST /v1/chat/completions`：对话接口
- `POST /api/direct-llm/chat`：首页智能体直连 LLM
- `POST /api/direct-llm/companion-chat`：角色直连对话
- `POST /api/models/*`：模型创建、详情、更新、删除、选择、清历史、自动绑骨
- `POST /api/hunyuan3d/generate`：图生/文生 3D 代理接口
- `POST /api/emotion-report`：情绪趋势报告

## 常用端口

| 端口 | 用途 |
|---|---|
| `5002` | Flask 主服务 |
| `5000` | 常见代理入口（如经 Nginx 暴露） |
| `5010` | MCP 管理服务 |
| `5001` | GenAgents 页面 |
| `10002` | 数字人 WebSocket |
| `10003` | Web/UI WebSocket |
| `9001` | Socket bridge |
| `5173` | Vite 前端开发端口 |
| `5011` | `schedule_manager` Web 管理页 |

## 数据存储

### SQLite

- `memory/fay.db`：对话、情绪等会话数据
- `memory/user_profiles.db`：用户、角色、模型信息
- `memory/auth.db`：后台登录信息

### 文件数据

- `memory/User_*/meta.json`
- `memory/User_*/memory_stream/nodes.json`
- `memory/User_*/memory_stream/embeddings.json`
- `models/`：3D 模型与动作文件
- `samples/`：音频样本
- `logs/`：运行日志

## 推荐工作流

### 对话工作流

1. 用户输入文本或语音
2. ASR 将语音转成文本
3. 后端进入 `Interact -> FeiFei -> nlp_cognitive_stream`
4. 结合角色设定、历史消息、长期记忆与 MCP 工具生成回复
5. WebSocket 推送文本和状态
6. TTS 合成语音
7. 前端接收文本、音频和动作状态，驱动 3D 角色表现

### 角色创建工作流

1. 前端输入文本描述或上传参考图
2. 后端调用 `/api/hunyuan3d/generate`
3. 生成基础 `glb` 模型
4. 调用自动绑骨服务
5. 生成 `source.glb / idle.glb / talking.glb / wave.glb`
6. 保存到 `models/` 并写回模型信息
7. 前端加载并用于互动展示

## 常见问题

### 1. 前端连不上后端

优先检查：

- 后端是否已启动
- 当前访问地址是否真的是后端入口地址
- `soullink/.env.local` 是否配置正确
- 管理页中的 API 地址是否已改成当前机器可访问地址
- 移动端是否误用了 `127.0.0.1`

### 2. 语音不可用

优先检查：

- `ASR_mode` 与 `tts_module` 是否配置正确
- 麦克风是否可用
- 阿里云 / 微软 / 火山等密钥是否可用
- `pyaudio` 和系统音频依赖是否安装成功

### 3. 图生 3D / 文生 3D 失败

优先检查：

- `hunyuan3d_api_url` 是否可访问
- 请求体是否过大，被代理层拦截
- 前端代理地址与真实后端地址是否一致

### 4. 自动绑骨失败

优先检查：

- `make_it_animatable_api_url` 是否可访问
- 生成的源模型文件是否真实写入 `models/`
- 当前前端调用的是否是同一个后端实例

## 开发建议

- 新人优先从 `main.py`、`gui/flask_server.py`、`core/fay_core.py`、`soullink/App.tsx` 开始阅读
- 如果要扩展工具能力，优先看 `faymcp/` 和 `mcp_servers/`
- 如果要扩展角色工作流，优先看 `soullink/services/modelService.ts`、`soullink/services/hunyuan3dService.ts`
- 如果要扩展动作处理，优先看 `mesh2motion/`

## 注意事项

- `system.conf` 中通常包含敏感配置，提交代码前务必脱敏
- `memory/`、`logs/`、`samples/`、`models/` 中包含运行期数据，不建议直接当作静态源码处理
- `soullink/` 与根目录后端是协作关系，不是互相替代关系
- 如果仓库里已经写入真实 API Key，建议立即更换并改为本地私有配置

## 相关文档

- `docs/system_architecture_overview.md`
- `docs/workflow_integration_guide.md`
- `mcp_servers/schedule_manager/README.md`
- `mcp_servers/character_workflow/README.md`
- `soullink/DEPLOY_ANDROID.md`
- `soullink/DOMAIN_CONFIG_GUIDE.md`

## 一句话总结

SoulLink 是一个“Python 后端编排 + 多模态能力接入 + 3D 角色资产生成 + React/Three.js 互动前端 + Android 封装”的数字人系统工程。
