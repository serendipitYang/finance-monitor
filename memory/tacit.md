# 🧠 隐性知识库 (Tacit Knowledge)

> 记录 Thomas 的偏好、过去的错误、安全规则和教训。
> 这是我的"经验积累"，每次犯错或学到新东西都要更新。

_最后更新：2026-02-23_

---

## 👤 Thomas 的偏好

### 工作风格
- 喜欢我**主动做事**，不要总是问他"你想要哪个方案？"——先尝试，搞不定再问
- 希望我能**独立操作浏览器**，包括申请账号、付款、发布等高级操作
- 沟通风格：直接、高效，不需要过多解释和废话
- 双语：中英文混用，随意切换

### 技术偏好
- 远程访问：**Parsec 优先**（低延迟），向日葵备用
- 网络：**Tailscale 内网**（不暴露公网）
- 不喜欢 VNC（配置麻烦，连接不稳定）

---

## ⚠️ 安全规则

### 授权边界
- **可以自由做的：** 读文件、搜索网页、Shell 命令、操作本机应用
- **需要确认的：** 发邮件、发推特、公开发布、付款操作
- **永远不做的：** 泄露私人数据、在群聊中代表 Thomas 发言

### 凭证安全
- sudo 密码、邮箱密码等**不存储在明文文件里**（docs/credentials.md 用 REDACTED）
- Gateway token 已配置，存在 config 文件中
- Tailscale 通过 GitHub OAuth 认证

### 多用户隔离
- Thomas 和 Joanna 使用**不同 Chrome Profile**
- 不在 Joanna 的 session 里暴露 Thomas 的数据

---

## ❌ 过去的错误和教训

### 2026-02-22：Browser 工具不稳定
**问题：** browser 工具的 tab 经常在操作后断开（"tab not found"）
**原因：** Chrome 扩展 relay 连接不稳定；每次用 `open` 打开新 tab 后，下一次操作就找不到了
**教训：**
- 用 `browser.open()` 拿到 targetId 后，**所有后续操作都传入该 targetId**
- 不要 focus 后再 snapshot，直接带 targetId 操作
- Gmail 等复杂 SPA 页面需要等待加载（wait 2-3秒）

### 2026-02-22：sudo 密码通过 echo pipe 失败
**问题：** `echo 'password' | sudo -S command` 第一次不工作
**原因：** 某些命令路径不在 sudo 的 PATH 里（如 `screencapture`、`systemsetup`、`lsof`）
**教训：** 用全路径，如 `/usr/sbin/screencapture`、`/usr/sbin/systemsetup`

### 2026-02-22：Tailscale Funnel vs Serve
**问题：** 开始把 Gateway 设置成 Funnel（公网暴露），有安全风险
**修复：** 改为 `serve` 模式（仅 tailnet 内访问）
**教训：** 默认用最小权限，不要暴露公网

### 2026-02-22：gog OAuth 需要手动授权
**问题：** `gog auth login` 会打开浏览器，但我无法自动完成 Google OAuth 授权
**原因：** Google OAuth 需要用户点击"允许"，无法绕过
**教训：** 提前让 Thomas 完成 OAuth 授权，之后我才能自动使用 API

### 2026-02-22：Peekaboo 权限
**问题：** Peekaboo 需要 Screen Recording + Accessibility 权限，但添加 Terminal 不够，需要添加 peekaboo 二进制本身
**路径：** `/opt/homebrew/bin/peekaboo`
**状态：** 待完成

### 2026-02-22：Gmail SMTP 无法直接使用账户密码
**问题：** 没有 2FA 的 Gmail 账号无法使用 SMTP（App Password 不可用，直接密码被拒）
**解决方案：** 开启 2FA 后生成 App Password，或者使用 Gmail API (gog)

---

## 💡 效率经验

### Shell 环境
- 很多系统命令不在默认 PATH，需要用全路径
  - `screencapture` → `/usr/sbin/screencapture`
  - `ifconfig` → `/sbin/ifconfig`
  - `netstat` → `/usr/sbin/netstat`
  - `lsof` → `/usr/sbin/lsof`

### Chrome 自动化
- browser 工具要传入 `targetId` 保持连接稳定
- AppleScript 操作 Chrome 需要开启 "View → Developer → Allow JavaScript from Apple Events"
- 复杂页面（Gmail）需要等待加载时间

### OpenClaw 命令
- `openclaw config set` 路径需要和 config schema 匹配（如 `channels.telegram.dmPolicy` 而非 `telegram.dmPolicy`）
- 修改 config 后需要 `openclaw gateway restart`
- `tailscale` CLI 默认不在 PATH，需要用 `/opt/homebrew/bin/tailscale`
- **Brave Search API:** 通过 Control UI 输入，Gateway 重启后生效

---

## 🔧 2026-02-23：Browser 工具稳定性解决方案

**问题：** `profile="chrome"` 经常断开，报错 "tab not found" 或 "pairing required"

**根本原因：**
- Chrome 扩展 relay 需要用户手动点击 toolbar 图标 attach tab
- 自动化流程中无法保证连接稳定性

**解决方案：**
- ✅ **使用 `profile="openclaw"`** — OpenClaw 管理的浏览器，自动启动，无需手动 attach
- ⚠️ **避免 `profile="chrome"`** — 仅用于需要用户已登录状态的特定任务（如已登录的 Gmail）

**代码示例：**
```javascript
// ✅ 推荐：稳定
browser({ action: "open", profile: "openclaw", targetUrl: "..." })

// ❌ 避免：需要手动 attach
browser({ action: "open", profile: "chrome", targetUrl: "..." })
```

**故障排除：**
- "tab not found" → 检查 Gateway 状态：`openclaw status`
- "pairing required" → sub-agent 未配置或 browser 服务未启动
- Chrome 崩溃 → 重启 Gateway：`openclaw gateway restart`

---

## 🤖 2026-02-23：Multi-Agent 架构现状

**现状：**
- 已设计完整架构（ARCHITECTURE.md + 3 个 sub-agent 文档）
- 但实际只有 `main` agent 存在于 OpenClaw 配置中
- `sessions_spawn` 调用 sub-agent 会报错 "pairing required"

**原因：**
- OpenClaw 的 agent 配置需要在 `~/.openclaw/agents/` 目录下创建独立配置
- 或者使用 `mode="run"` 直接运行无需预注册

**两种模式：**
1. **预注册模式：** 在 `~/.openclaw/agents/` 创建 `researcher/` 目录和配置
2. **直接运行模式：** `sessions_spawn({ agentId: "researcher", mode: "run", ... })` 无需预注册

**推荐：** 对于简单任务，直接用 `mode="run"`；需要持久化状态再用预注册模式

---

## 🧠 2026-02-23：Epistemic Honesty (认知诚实)

**核心原则：** Fluent output ≠ accuracy (流畅输出 ≠ 准确性)

**易编造的高风险内容：**
- 研究论文名称、具体统计数据
- API 版本号、CLI 参数、URL
- 具体日期、截止后的事件

**不确定性信号：**
- "I just read this in the codebase" — 高置信度，主要来源
- "This is a stable pattern" — 高置信度，基础知识
- "The general approach is..." — 中等置信度，无具体引用
- "As of my knowledge cutoff..." — 承认时效性
- "I'd want to verify this" — 诚实的不确定性
- "My hypothesis is..." — 正在调查，非结论

**搜索 vs 记忆的决策（时效性测试）：**
- **稳定概念**（不搜索）：语言基础、算法、已建立的模式、不变的历史事实
- **时效敏感**（先搜索）：产品发布、API 版本、当前法规、最近事件、价格

**The cost of not searching is WAY higher than the cost of searching.**

---

## 📊 2026-02-23：Web Search 配置

**Brave Search API 配置：**
- 通过 Control UI 输入 API key
- Gateway 重启后生效：`openclaw gateway restart`
- 环境变量：`BRAVE_API_KEY` 需要设置在 Gateway 进程中

**验证：** `web_search({ query: "test" })` 应返回结果而非 "missing_brave_api_key"

---

## 🎯 2026-02-23：决策框架 (from TechNickAI)

**记忆四标准：**
1. **Durability** — 30天后还重要吗？
2. **Uniqueness** — 新的还是已记录的？
3. **Retrievability** — 以后想回忆吗？
4. **Authority** — 可靠吗？

**Bezos 双向门：**
- **双向门**（易撤销）→ 自由行动：读文件、探索、搜索、编辑配置
- **单向门**（难撤销）→ 暂停确认：发邮件、发推、购买、删除文件

**决策因素（按顺序）：**
1. **来源：** 主要来源（文件、文档、网页）> 记忆（具体信息）
2. **时效性：** 时间敏感？稳定概念老化好；API 不行
3. **可验证性：** 能确认对吗？
4. **可逆性：** 容易撤销？Git revert = 容易；已发邮件 = 不行
5. **影响范围：** 一个文件 vs 整个工作区 vs 外部系统

---

## 📝 2026-02-23：Sub-Agent 委托规则

**何时 spawn sub-agent：**
- 跨多个文件/来源探索或搜索
- 需要多轮搜索的研究任务
- 决策前需要大量信息收集
- 可在后台运行的工作
- 浏览器自动化、复杂 web 任务、多步配置

**为什么：** 保留主上下文窗口用于协调和决策

**如何：**
```javascript
sessions_spawn({
  task: "[完整上下文 + 具体任务]",
  agentId: "researcher" | "browser-operator" | "coder",
  mode: "run",
  thread: true
})
```
