# 🦅 峨眉峰 Multi-Agent Architecture

> 设计原则：主 session 轻量（理解+调度），重活派给 sub-agent。
> Token 不烧在上下文积累上，烧在真正的执行上。

_版本：v0.1 — 2026-02-23_

---

## 架构总览

```
Thomas (Telegram)
       │
       ▼
  ┌─────────────────────────┐
  │   Zecheng / main        │  ← 你的主界面，永远在这里
  │   理解意图 + 任务分发     │  ← session 保持轻量
  │   汇总结果 + 记忆更新     │
  └────────────┬────────────┘
               │ sessions_spawn
    ┌──────────┼──────────────┐
    ▼          ▼              ▼
┌────────┐ ┌────────┐  ┌──────────┐
│research│ │browser │  │  coder   │  ← 专用 sub-agent
│  🔬   │ │  🌐    │  │    💻    │  ← 隔离执行，不污染主session
└────────┘ └────────┘  └──────────┘
```

**关键设计决策：**
- 用 `sessions_spawn` 而非新 Telegram bot — 零额外配置
- 每个 sub-agent 有自己的 system prompt 文件（在 `agents/` 目录）
- 主 session 只负责「输入理解 → 分发 → 结果汇总」三步
- Sub-agent 完成后自动 push 结果回主 session

---

## Sub-Agent 定义

### 🔬 researcher
**触发场景：** 深度调研、多页面信息汇总、长文档分析
**模型：** Kimi（长 context，便宜）
**工具：** web_search, web_fetch, read, write
**配置：** `agents/researcher.md`

### 🌐 browser-operator  
**触发场景：** 浏览器登录、表单填写、网页操作、截图
**模型：** Sonnet（需要推理能力处理 UI）
**工具：** browser, exec, read, write
**配置：** `agents/browser-operator.md`

### 💻 coder
**触发场景：** 写脚本、调试代码、文件操作、系统配置
**模型：** Sonnet 或 cheaper coding model
**工具：** read, write, edit, exec
**配置：** `agents/coder.md`

### 📧 comms _(暂缓，先做前三个)_
**触发场景：** 邮件起草、社交媒体发布、消息撰写
**模型：** Kimi

---

## 任务分发规则（我遵守的协议）

```
收到任务
  │
  ├─ 简单/快速（< 2 steps）→ 直接在主 session 处理
  │
  ├─ 调研/信息收集 → spawn researcher
  │    等待结果 → 汇总给 Thomas
  │
  ├─ 浏览器操作 → spawn browser-operator
  │    等待结果 → 汇总给 Thomas
  │
  └─ 代码/脚本 → spawn coder
       等待结果 → 汇总给 Thomas
```

**什么时候直接做（不派发）：**
- 单步操作（查天气、读文件、发消息）
- 需要和 Thomas 来回确认的任务（对话密集型）
- 时间敏感（< 30 秒能搞定的）

---

## 目录结构

```
workspace/
└── agents/
    ├── ARCHITECTURE.md     ← 本文件，总体设计
    ├── researcher.md       ← researcher sub-agent system prompt
    ├── browser-operator.md ← browser sub-agent system prompt
    └── coder.md            ← coder sub-agent system prompt
```

---

## 阶段计划

- [x] **Phase 0** — 架构设计（本文档）
- [ ] **Phase 1** — 写三个 sub-agent 的 system prompt
- [ ] **Phase 2** — 测试：派一个真实任务给 researcher
- [ ] **Phase 3** — 建立分发习惯，写入 AGENTS.md 作为我的行为规范
- [ ] **Phase 4** — 回顾效果，迭代优化

---

## 说明

这套架构**不需要新 Telegram bot 或 Gateway 重启**，完全基于现有 `sessions_spawn` 能力。
未来如果某个 agent 需要完全独立的记忆和身份（比如 Joanna 专属助手），
再考虑升级为 `openclaw agents add` 的持久 agent。
