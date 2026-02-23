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
