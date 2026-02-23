# 🗂️ 活跃项目跟踪 (Active Projects)

> 参考 Tiago Forte PARA 方法。只放当前进行中的项目，完成的归档到 archive/。

_最后更新：2026-02-23_

---

## 🔥 进行中

### [P1] 无头工作站基础设施
**目标：** 完成 Mac mini 工作站的所有基础配置，让 Thomas 能完全远程管理我。
**状态：** 🟡 进行中
**进展：**
- ✅ 无头模式（显示器已断开）
- ✅ Parsec 远程桌面（主要访问方式）
- ✅ 向日葵（Joanna 备用）
- ✅ Tailscale（安全内网）
- ✅ Telegram 连接
- ✅ 三层知识库（本文件）
- ✅ Brave Search API 配置
- ⚠️ Browser 工具不稳定（openclaw profile 可用但易断）
- ✅ Gmail 可通过 browser 发送（需手动登录）
- ✅ Peekaboo 权限已修复
- ❌ Multi-agent 未配置（仅 main 存在）

**待办：**
- [ ] 修复 browser 工具稳定性（Gateway 级别问题）
- [ ] 配置 gog OAuth（Gmail API）
- [ ] 注册 sub-agents（researcher, browser-operator, coder）

---

### [P3] Instagram 博主研究
**目标：** 找 LA/Torrance 地区 foodie/lifestyle Instagram 博主
**状态：** ✅ 数据收集完成，待补充 15 位
**交付：**
- 45 位博主 (1k-10k followers) → `memory/data/instagram-research/`
- 40 位博主 (10k-30k followers) → 可筛选至 30 位
- CSV 文件已发送给 Thomas

**待办：**
- [ ] 补充 15 位 1k-10k 范围博主
- [ ] 与现有 Google Sheet 去重

---

### [P2] 知识库系统
**目标：** 建立 Tiago Forte 三层记忆系统 + 每日 2:45 自动梳理 cron job。
**状态：** 🟢 核心结构已完成
**已完成：**
- ✅ Daily notes 系统 (`memory/YYYY-MM-DD.md`)
- ✅ Tacit knowledge 文件 (`memory/tacit.md`)
- ✅ 项目跟踪 (`memory/projects.md`)
- ✅ 长期记忆 (`MEMORY.md`)
- ✅ Instagram 研究数据存档 (`memory/data/`)

**待办：**
- [ ] 注册每日梳理 cron job
- [ ] 测试自动摘要发送

---

## 📋 待启动

### [P3] Joanna 工作环境配置
**目标：** 让 Joanna 能从中国稳定连接并使用 Mac mini 工作。
**待办：**
- [ ] 测试向日葵连接稳定性
- [ ] 配置 Chrome Profile 2（Joanna 专用）
- [ ] 邀请 Joanna 加入 Tailscale tailnet（可能需要翻墙）

### [P4] OpenClaw 更新
**待办：**
- [ ] 更新到 2026.2.22-2

---

### [P5] 金融监控系统 ⭐ NEW
**目标:** 自动监控股票组合，实时警报 + 每日简报
**状态:** 🟡 Phase 1 进行中
**持仓:** NVDA, TQQQ, MU, BTC, FIG, KLAR, AIRO, RVI

**已完成:**
- ✅ 每日 8:30 AM 简报 cron job (ID: bae49a41-5a96-45b0-8924-2ace84479a9f)
- ✅ 持仓配置文件 (portfolio.csv)
- ✅ 系统架构设计
- ✅ 警报规则定义

**待办:**
- [ ] 安装 finance-news-openclaw-skill
- [ ] 开发实时价格监控脚本
- [ ] 配置每小时价格检查
- [ ] 开发 Stock Analyst Agent
- [ ] 测试警报推送

**警报条件:**
- 股价波动 > ±5%
- 成交量 > 200% 均值
- 重大新闻/事件

---

## ✅ 已完成归档

_(移到 memory/archive/ 目录)_
