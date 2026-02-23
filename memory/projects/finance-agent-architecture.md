# 🤖 金融 Agent 架构设计

**创建日期:** 2026-02-23  
**目标:** 自动监控股票组合，发送实时警报和每日简报

---

## 📋 需求总结

**Thomas 的要求:**
1. ✅ 每天 8:30 AM 发送新闻摘要 + 股票持仓信息
2. ✅ 自动盯盘 (金融 agent)
3. ✅ 股票分析师 agent
4. ✅ 监控标的: NVDA, FIG, KLAR, AIRO, TQQQ, MU, RVI, BTC
5. ✅ 警报条件: 重大事件、新闻、股价重大波动(±5%)、超额换手(>200%)

---

## 🏗️ Agent 架构

```
┌─────────────────────────────────────────────────────────────┐
│                    金融监控系统                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────┐      ┌──────────────────┐           │
│  │  Financial       │      │  Stock Analyst   │           │
│  │  Monitor Agent   │      │  Agent           │           │
│  │  (financial-mon) │      │  (stock-analyst) │           │
│  └────────┬─────────┘      └────────┬─────────┘           │
│           │                         │                      │
│           ▼                         ▼                      │
│  ┌──────────────────────────────────────────┐             │
│  │          Data Sources                    │             │
│  │  ┌────────┐ ┌────────┐ ┌────────────┐  │             │
│  │  │ Yahoo  │ │ News   │ │ CoinGecko  │  │             │
│  │  │ Finance│ │ API    │ │ (BTC)      │  │             │
│  │  └────────┘ └────────┘ └────────────┘  │             │
│  └──────────────────────────────────────────┘             │
│           │                         │                      │
│           ▼                         ▼                      │
│  ┌──────────────────────────────────────────┐             │
│  │          Alert Engine                    │             │
│  │  • Price threshold checks                │             │
│  │  • Volume anomaly detection              │             │
│  │  • News sentiment analysis               │             │
│  └──────────────────────────────────────────┘             │
│           │                         │                      │
│           ▼                         ▼                      │
│  ┌──────────────────────────────────────────┐             │
│  │          Delivery                        │             │
│  │  • Telegram (Thomas)                     │             │
│  │  • Daily briefing (8:30 AM)              │             │
│  │  • Real-time alerts (immediate)          │             │
│  └──────────────────────────────────────────┘             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 组件详解

### 1. Financial Monitor Agent (financial-monitor)

**职责:**
- 每小时检查股价和成交量
- 检测异常波动并触发警报
- 监控新闻源获取相关资讯
- 生成每日 8:30 AM 简报

**触发逻辑:**
```python
# 价格警报
if price_change > 5% or price_change < -5%:
    send_alert(f"🚨 {symbol} 大涨/大跌 {price_change}%")

# 成交量警报
if volume > avg_volume * 2:
    send_alert(f"📊 {symbol} 成交量异常 {volume}x")

# 新闻警报
if breaking_news and symbol in portfolio:
    send_alert(f"📰 {symbol}: {news_title}")
```

**Cron 设置:**
```bash
# 每日简报 (8:30 AM CST) - ✅ 已配置
30 8 * * * daily-market-briefing

# 每小时价格检查 (待配置)
0 * * * * price-check
```

---

### 2. Stock Analyst Agent (stock-analyst)

**职责:**
- 深度分析持仓股票基本面
- 跟踪分析师评级变化
- 监控行业趋势和竞争动态
- 生成周度投资洞察报告

**输出:**
- 每周一次深度分析报告 (周日 9 AM)
- 重大事件即时分析
- 技术面/基本面评分

**分析框架:**
```markdown
## 股票分析报告: NVDA

### 基本面评分: 8.5/10
- 收入增长: +120% YoY
- 利润率: 78% (行业领先)
- 现金流: 强劲
- 债务水平: 低

### 技术面评分: 7.2/10
- 趋势: 上升趋势
- 支撑/阻力: $850 / $920
- RSI: 65 (中性偏强)
- 成交量: 高于均值

### 催化剂
- 下周财报 (预期 EPS $5.20)
- Blackwell 芯片发布进展
- 中国出口管制影响

### 风险因素
- 估值偏高 (P/E 65x)
- 地缘政治风险
- 竞争加剧 (AMD, Intel)

### 建议
中期持有，关注财报后动向
```

---

## 📊 数据源

### 股价数据
| 来源 | 类型 | 频率 | 成本 |
|------|------|------|------|
| Yahoo Finance API | 股票/ETF | 实时 | 免费 |
| Alpha Vantage | 股票/ETF | 延迟15分钟 | 免费 (500 req/day) |
| CoinGecko API | 加密货币 | 实时 | 免费 |

### 新闻数据
| 来源 | 类型 | 语言 |
|------|------|------|
| NewsAPI | 综合财经 | 英文 |
| GNews | 综合财经 | 多语言 |
| Reuters RSS | 专业财经 | 英文 |
| Bloomberg API | 专业财经 | 英文 (付费) |

### 分析数据
| 来源 | 内容 |
|------|------|
| Seeking Alpha | 分析师文章 |
| MarketWatch | 市场新闻 |
| TradingView | 技术分析 |
| SEC EDGAR | 监管文件 |

---

## 🚨 警报规则

### Level 1: 紧急 (立即发送)
- 股价波动 > ±5%
- 成交量 > 200% 均值
- 重大新闻 (并购、CEO变动、监管)
- 财报发布

### Level 2: 重要 (5分钟内发送)
- 分析师评级大幅调整
- 行业政策变化
- 大额 insider trading

### Level 3: 常规 (每日简报包含)
- 一般新闻
- 技术面突破
- 市场情绪变化

---

## 🔌 推荐的 OpenClaw Skills

### 1. finance-news-openclaw-skill ⭐ (kesslerio)
**状态:** 已发现，待安装
**功能:**
- 多源新闻聚合 (Reuters, WSJ, Bloomberg, CNBC)
- 组合跟踪与价格警报
- 自动简报生成
- Telegram/WhatsApp 推送
- 支持德语/英语

**安装:**
```bash
git clone https://github.com/kesslerio/finance-news-openclaw-skill.git \
  ~/.openclaw/skills/finance-news
```

### 2. 自定义监控脚本 (待开发)
**功能:**
- Yahoo Finance API 集成
- 实时价格监控
- 成交量异常检测
- 新闻情绪分析

---

## 📱 消息格式

### 每日简报 (8:30 AM)
```
📊 早安简报 - 2026-02-24

全球市场:
• S&P 500: +0.8% | NASDAQ: +1.2% | DOW: +0.5%

持仓动态:
🟢 NVDA: +3.2% ($875.50) - AI芯片需求强劲
🔴 TQQQ: -2.1% ($45.30) - 纳斯达克回调
🟢 BTC: +5.8% ($58,200) - ETF资金流入

重大新闻:
• NVIDIA盘后发布财报，市场预期EPS $5.20
• 美联储官员发言，暗示维持利率不变

今日关注:
• 10:00 AM EST - 消费者信心指数
• NVDA 盘后财报
```

### 实时警报
```
🚨 股价警报

NVDA 大涨 +6.5%
当前价: $890.20 (+$54.30)
触发: 突破 52周新高
成交量: 350% 均值 (异常活跃)

相关新闻:
• [Reuters] NVIDIA宣布Blackwell芯片提前量产
• [CNBC] 分析师上调目标价至$1,100

技术面:
• RSI: 72 (进入超买区域)
• 突破阻力位 $875

建议: 关注持续性，考虑分批止盈
```

---

## 🛠️ 实施计划

### Phase 1: 基础设施 (本周)
- [x] 创建持仓配置文件
- [x] 设置每日 8:30 AM cron job
- [ ] 安装 finance-news skill
- [ ] 配置 Telegram bot 推送

### Phase 2: 实时监控 (下周)
- [ ] 开发价格监控脚本
- [ ] 配置每小时价格检查
- [ ] 实现异常检测算法
- [ ] 测试警报推送

### Phase 3: 分析师 Agent (第3周)
- [ ] 开发基本面分析模块
- [ ] 集成分析师评级 API
- [ ] 创建周度报告生成器
- [ ] 配置周日 9 AM 定时任务

### Phase 4: 优化 (第4周)
- [ ] 优化警报准确性 (减少噪音)
- [ ] 添加更多技术指标
- [ ] 实现回测功能
- [ ] 创建仪表盘

---

## 📝 文件清单

| 文件 | 路径 | 状态 |
|------|------|------|
| 组合配置 | `memory/data/portfolio-config.md` | ✅ 已创建 |
| 持仓 CSV | `memory/data/portfolio.csv` | ✅ 已创建 |
| Agent 设计 | `memory/projects/finance-agent-architecture.md` | ✅ 已创建 |
| 警报历史 | `memory/data/stock-alerts/` | 待创建 |
| 分析报告 | `memory/projects/stock-analysis/` | 待创建 |
| Skill 配置 | `skills/finance-news/` | 待安装 |

---

## 🔗 相关资源

- **GitHub:** kesslerio/finance-news-openclaw-skill
- **GitHub:** BankrBot/openclaw-skills (crypto/DeFi)
- **Cron Job:** bae49a41-5a96-45b0-8924-2ace84479a9f
- **Portfolio:** memory/data/portfolio.csv

---

## ✅ 当前状态

| 组件 | 状态 |
|------|------|
| 每日 8:30 AM 简报 | ✅ 已配置 |
| 持仓数据文件 | ✅ 已创建 |
| 监控 Agent | ⏳ 待开发 |
| 分析师 Agent | ⏳ 待开发 |
| 实时警报 | ⏳ 待配置 |
| finance-news skill | ⏳ 待安装 |

---

*下次更新: 完成 Phase 1 后*
