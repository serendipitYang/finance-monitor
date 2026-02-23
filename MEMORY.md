# MEMORY.md - Zecheng 长期记忆

> 参考 Tiago Forte PARA 方法建立。这里是蒸馏后的核心记忆，不是流水账。
> 详细日志在 memory/YYYY-MM-DD.md，项目在 memory/projects.md，教训在 memory/tacit.md。

_最后更新：2026-02-23_

---

## 我是谁

- **名字：** Zecheng Yu（峨眉峰 / Emei Peak）🦅
- **家：** Mac mini (Emei-Peaks-Mac-mini.local)，Thomas 专门为我买的
- **Boss：** Thomas Yang (thomasyh95@gmail.com, Telegram: 8798947736)
- **同事：** Joanna（会远程用这台 Mac mini 工作，用向日葵从中国连接）
- **模型：** Claude Sonnet 4.6（2026-02-23 从 Kimi 切换）

---

## 工作站基础设施

| 服务 | 状态 | 详情 |
|------|------|------|
| Parsec | ✅ | https://parsec.gg/g/3A3YiWwfMY3NsEJngsrzh6wNdJi/ab19ebb1/ |
| Tailscale | ✅ | serve 模式，IP: 100.120.109.51 |
| Telegram | ✅ | @EmeiPeak_bot，Thomas ID: 8798947736 |
| 向日葵 | ✅ | Joanna 备用，无人值守已开 |
| OpenClaw | ✅ | http://100.120.109.51:18789/ |
| 无头模式 | ✅ | 显示器已断开，Parsec 操作 |

---

## 知识库系统（2026-02-23 建立）

### 三层结构
1. **每日笔记** → `memory/YYYY-MM-DD.md`：每天做了什么
2. **活跃项目** → `memory/projects.md`：当前任务清单
3. **隐性知识** → `memory/tacit.md`：偏好、错误、教训、安全规则

### 自动化
- **Cron Job：** 每天凌晨 2:45（America/Chicago）自动梳理
- Job ID: `20147b79-d508-4d03-9f57-7bcbca44b4be`
- Job Name: `daily-knowledge-consolidation`
- 完成后发 Telegram 摘要给 Thomas

---

## Thomas 的核心需求

1. **我能独立操作浏览器**：浏览、发布、申请账号、付款
2. **主动做事**：不要总问，先尝试，搞不定再问
3. **Joanna 和 Thomas 完全隔离**：不同 Chrome Profile，数据不混用

---

## 当前未解决的关键问题

1. **Browser 工具不稳定**：tab 经常断开（最高优先级修复）
2. ~~**Gmail 自动发送**~~：✅ 已解决 — 使用 `openclaw` 浏览器 profile 登录 yhan65905@gmail.com，通过 `browser` 工具直接操作 Gmail 网页发送邮件
3. ~~**Peekaboo 权限**~~：✅ 已修复 — 给 Node.js (`/opt/homebrew/Cellar/node/25.6.1/bin/node`) 添加 Screen Recording 权限
