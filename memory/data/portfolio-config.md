# 💼 Thomas 股票投资组合配置

**创建日期:** 2026-02-23  
**监控状态:** 活跃

---

## 📊 持仓股票清单

| 代码 | 公司名称 | 类型 | 监控重点 |
|------|---------|------|----------|
| NVDA | NVIDIA | 科技股/AI芯片 | 财报、AI需求、数据中心增长 |
| FIG | - | - | 待确认完整代码 |
| KLAR | - | - | 待确认完整代码 |
| AIRO | - | - | 待确认完整代码 |
| TQQQ | ProShares UltraPro QQQ | 3倍杠杆ETF | 纳斯达克波动、杠杆损耗 |
| MU | Micron Technology | 存储芯片 | 内存周期、AI存储需求 |
| RVI | - | - | 待确认完整代码 |
| BTC | Bitcoin | 加密货币 | 监管政策、ETF流动、减半周期 |

---

## 🔔 报警触发条件

### 股价波动
- **单日涨幅** > 5% → 发送提醒
- **单日跌幅** > 5% → 发送提醒  
- **连续3日涨跌** > 10% → 紧急提醒

### 成交量异常
- **超额换手** > 200% 日均成交量 → 发送提醒
- **放量突破/跌破** 关键价位 → 技术分析提醒

### 重大事件
- **公司公告** (财报、并购、管理层变动)
- **行业新闻** (政策变化、技术突破)
- **分析师评级** 上调/下调
- **SEC文件** (13F、 insider trading)

### 加密货币特定 (BTC)
- 价格突破/跌破关键心理价位 ($50K, $60K, $70K等)
- 大额钱包流动 (鲸鱼警报)
- 监管政策变化
- ETF资金流向

---

## 📰 新闻摘要配置

### 每日简报 (8:30 AM CST)
**内容包含:**
1. 全球市场概览 (S&P 500, NASDAQ, DOW)
2. 持仓股票 overnight 价格变动
3. 相关新闻摘要 (AI、芯片、加密货币)
4. 今日重点关注事项

### 信息来源
- **财经新闻:** Reuters, Bloomberg, CNBC, Yahoo Finance
- **加密新闻:** CoinDesk, CoinTelegraph
- **分析师报告:** Seeking Alpha, MarketWatch

---

## 🤖 Agent 配置

### 1. 金融监控 Agent (financial-monitor)
**职责:**
- 每小时检查股价和成交量
- 检测异常波动并触发警报
- 监控新闻源获取相关资讯
- 生成每日 8:30 AM 简报

**触发条件:**
```
价格变动 > ±5% → 立即发送 Telegram
成交量 > 200% 均值 → 立即发送 Telegram
重大新闻发布 → 立即发送 Telegram
每日 8:30 AM → 发送市场简报
```

### 2. 分析师 Agent (stock-analyst)
**职责:**
- 深度分析持仓股票基本面
- 跟踪分析师评级变化
- 监控行业趋势和竞争动态
- 生成周度投资洞察报告

**输出:**
- 每周一次深度分析报告 (周日)
- 重大事件即时分析
- 技术面/基本面评分

---

## 🔧 技术实现

### 使用的 Skills
1. **finance-news-openclaw-skill** (kesslerio)
   - 多源新闻聚合
   - 组合跟踪与价格警报
   - Telegram/WhatsApp 推送

2. **自定义监控脚本** (待开发)
   - Yahoo Finance API 实时价格
   - 成交量异常检测
   - 新闻情绪分析

### API 需求
- Yahoo Finance API (免费) - 股价数据
- NewsAPI / GNews - 新闻聚合
- CoinGecko API (免费) - 加密货币数据
- Telegram Bot API - 消息推送

### Cron Job 设置
```bash
# 每日简报 (8:30 AM CST)
30 8 * * * /usr/local/bin/finance-briefing

# 每小时价格检查
0 * * * * /usr/local/bin/price-check

# 每周分析师报告 (周日 9 AM)
0 9 * * 0 /usr/local/bin/weekly-analysis
```

---

## 📈 报告示例

### 每日简报格式
```
📊 早安简报 - 2026-02-24

全球市场:
• S&P 500: +0.8% | NASDAQ: +1.2% | DOW: +0.5%

持仓动态:
🟢 NVDA: +3.2% ($875.50) - AI芯片需求强劲
🔴 TQQQ: -2.1% ($45.30) - 纳斯达克回调
🟢 BTC: +5.8% ($58,200) - ETF资金流入

重大新闻:
• NVIDIA盘后发布财报，市场预期...
• 美联储官员发言，暗示利率...

今日关注:
• 10:00 AM EST - 消费者信心指数
• NVDA 盘后财报
```

### 实时警报格式
```
🚨 股价警报

NVDA 大涨 +6.5%
当前价: $890.20
触发: 突破 52周新高
成交量: 350% 均值

相关新闻:
• [Reuters] NVIDIA宣布新一代AI芯片...

建议: 关注是否持续突破，考虑止盈策略
```

---

## 📝 待办事项

- [ ] 安装 finance-news-openclaw-skill
- [ ] 配置 Telegram 推送
- [ ] 创建 portfolio.csv 持仓文件
- [ ] 设置每日 8:30 AM cron job
- [ ] 开发价格监控脚本
- [ ] 配置报警阈值
- [ ] 创建分析师 agent
- [ ] 测试完整流程

---

## 🔗 相关文件

- **持仓数据:** `memory/data/portfolio.csv`
- **历史记录:** `memory/data/stock-alerts/`
- **分析报告:** `memory/projects/stock-analysis/`
- **配置:** `tools/finance-config.yaml`
