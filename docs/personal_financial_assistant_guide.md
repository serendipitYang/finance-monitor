# 🤖 Personal Financial Assistant Agent 使用指南

**创建日期:** 2026-02-23  
**用途:** 专门处理股票监控、价格警报和财务分析任务

---

## ✅ 已完成配置

### 1. Agent 注册
```bash
$ openclaw agents list
Agents:
- main (default)
- personal_financial_assistant ✅
```

### 2. 文件位置
- **配置:** `~/.openclaw/agents/personal_financial_assistant.json`
- **系统提示:** `~/.openclaw/agents/personal_financial_assistant.md`
- **工作区:** `~/.openclaw/workspace`
- **状态目录:** `~/.openclaw/agents/personal_financial_assistant/`

### 3. 模型配置
- **模型:** Claude Sonnet 4.6
- **超时:** 300 秒
- **思考级别:** medium

---

## 🎯 任务分水岭设计

### 主会话 (main agent) 处理:
- 日常对话和问答
- 任务协调和委派
- 一般性研究
- 非财务类自动化

### Personal Financial Assistant 处理:
- ✅ 股票价格监控
- ✅ 价格警报检测 (±5%)
- ✅ 每日市场简报生成
- ✅ 财务新闻聚合
- ✅ 持仓分析
- ✅ 财报跟踪

---

## 🚀 使用方法

### 方法 1: 直接命令行启动 (推荐)

```bash
# 启动 finance agent 交互式会话
openclaw agents run personal_financial_assistant

# 或者在对话中调用
openclaw agents run personal_financial_assistant --message "Check portfolio alerts"
```

### 方法 2: 作为独立服务运行

```bash
# 后台运行 finance agent 监听任务
openclaw gateway start --agent personal_financial_assistant
```

### 方法 3: 从主会话委派 (待 Gateway 配置更新)

```javascript
// 当 Gateway 支持后，主会话可以调用:
sessions_spawn({
  agentId: "personal_financial_assistant",
  task: "Check stock alerts for NVDA, TQQQ, MU",
  mode: "run"
})
```

---

## 📊 当前能力

### 已配置功能
1. **实时股价监控** (yfinance)
2. **价格警报检测** (±5% 阈值)
3. **每日简报生成** (8:30 AM)
4. **RSS 新闻聚合** (WSJ, CNBC, Yahoo)
5. **持仓跟踪** (NVDA, TQQQ, MU, FIG, KLAR, AIRO, RVI, BTC)

### 待配置功能
- [ ] 自动每小时检查
- [ ] Telegram 实时推送
- [ ] 财报日历跟踪
- [ ] 分析师评级监控

---

## 💡 内存优化原理

### 问题
主会话处理所有任务，导致：
- 上下文膨胀
- 财务数据混入日常对话
- 股票历史记录占用 token

### 解决方案
```
┌─────────────────────────────────────────┐
│              主会话 (main)               │
│  - 日常对话                              │
│  - 任务协调                              │
│  - "检查我的股票" → 委派                  │
│  - 接收摘要报告                          │
└──────────────┬──────────────────────────┘
               │
               ▼ 委派 finance 任务
┌─────────────────────────────────────────┐
│   personal_financial_assistant          │
│  - 获取股价数据                          │
│  - 检测价格警报                          │
│  - 生成详细报告                          │
│  - 返回: "FIG -5.14%, 触发警报"          │
└─────────────────────────────────────────┘
```

**结果:**
- 主会话只保留财务摘要
- 详细数据在 sub-agent 中处理
- Token 使用更高效

---

## 🔧 测试命令

```bash
# 激活环境
eval "$(/opt/homebrew/bin/conda shell.zsh hook)"
conda activate finance

# 运行股价检查
cd ~/.openclaw/workspace/skills/finance-monitor
python finance_monitor.py --briefing

# 检查警报
python finance_monitor.py --alerts
```

---

## 📁 相关文件

- `~/.openclaw/agents/personal_financial_assistant.md` - Agent 系统提示
- `~/.openclaw/workspace/skills/finance-monitor/finance_monitor.py` - 监控脚本
- `~/.openclaw/workspace/memory/data/portfolio.csv` - 持仓配置
- `~/.openclaw/workspace/memory/data/portfolio-config.md` - 配置文档

---

*配置完成: 2026-02-23*
