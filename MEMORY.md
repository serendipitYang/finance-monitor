# MEMORY.md - Zecheng 长期记忆

> Curated essentials (~100 lines max). Hot context always loaded.  
> 详细日志在 `memory/YYYY-MM-DD.md`，项目在 `memory/projects.md`，教训在 `memory/tacit.md`。

_最后更新：2026-02-23_

---

## 我是谁

- **名字：** Zecheng Yu（峨眉峰 / Emei Peak）🦅
- **家：** Mac mini (Emei-Peaks-Mac-mini.local)
- **Boss：** Thomas Yang (Telegram: 8798947736)
- **同事：** Joanna（向日葵远程）
- **模型：** Claude Sonnet 4.6

---

## 工作站基础设施

| 服务 | 状态 | 详情 |
|------|------|------|
| Parsec | ✅ | https://parsec.gg/g/3A3YiWwfMY3NsEJngsrzh6wNdJi/ab19ebb1/ |
| Tailscale | ✅ | IP: 100.120.109.51 |
| Telegram | ✅ | @EmeiPeak_bot |
| Brave Search | ✅ | API key configured |
| Browser | ⚠️ | `openclaw` profile preferred; unstable at Gateway level |
| Multi-agent | ⚠️ | Designed, not registered |

---

## Thomas 的核心需求

1. **独立操作浏览器**：浏览、发布、申请账号、付款
2. **主动做事**：先尝试，搞不定再问
3. **Joanna/Thomas 完全隔离**：不同 Chrome Profile

---

## 知识库结构

```
memory/
├── active-context.md     # 工作记忆（当前热点）
├── projects.md           # 活跃项目
├── tacit.md              # 隐性知识（教训、偏好）
├── YYYY-MM-DD.md         # 每日笔记
├── projects/             # 项目详细文档
├── data/                 # 数据存档
└── learning/             # 学习资料
```

---

## 关键数据位置

- **Instagram 研究：** `memory/data/instagram-research/`
  - 45 位博主 (1k-10k)
  - 40 位博主 (10k-30k)

---

## 当前未解决

1. **Browser 工具**：Gateway 级别不稳定，需修复
2. **Multi-agent**：✅ 已配置 researcher, coder, browser-operator, **personal_financial_assistant**
3. **gog**：未 OAuth 认证

## 🤖 已配置 Sub-Agents

| Agent | 用途 | 模型 |
|-------|------|------|
| `researcher` | 深度调研、多源信息 | Claude Sonnet 4.6 |
| `coder` | 代码、脚本、系统配置 | Claude Sonnet 4.6 |
| `browser-operator` | 浏览器自动化 | Claude Sonnet 4.6 |
| `personal_financial_assistant` | **股票监控、价格警报、财务分析** | Claude Sonnet 4.6 |

**Finance 任务分水岭：**
- 所有股票监控、价格检查、财务分析任务 → 委派给 `personal_financial_assistant`
- 主会话只接收汇总报告，不处理细节

---

## 最近决策

- 2026-02-23: 使用 `profile="openclaw"` 作为 browser 主要方案
- 2026-02-23: 采用三层记忆结构（每日笔记/项目/隐性知识）
- 2026-02-23: 从 Kimi 切换到 Claude Sonnet 4.6

---

## 学习资源

- **OpenClaw 配置研究：** `memory/learning/openclaw-config-research.md`
- **最佳实践来源：** TechNickAI/openclaw-config, coolmanns/memory-architecture

---

_这是蒸馏后的核心记忆。详细信息在各层文件中。_
