# Stock Monitor Skill

监控股票价格、新闻，并发送警报

## 功能

- 每小时检查股价变动
- 检测异常成交量
- 聚合相关新闻
- 生成每日简报
- 发送 Telegram 警报

## 安装

```bash
# 安装依赖
pip install yfinance newsapi-python python-telegram-bot

# 配置文件
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="8798947736"
export NEWSAPI_KEY="your_newsapi_key"
```

## 使用

```bash
# 生成每日简报
python stock_monitor.py --briefing

# 检查价格变动
python stock_monitor.py --check-prices

# 检查新闻
python stock_monitor.py --check-news
```

## Cron 配置

```bash
# 每小时检查
0 * * * * cd ~/.openclaw/skills/stock-monitor && python stock_monitor.py --check-prices

# 每日简报 (8:30 AM CST)
30 8 * * * cd ~/.openclaw/skills/stock-monitor && python stock_monitor.py --briefing
```

## 配置

编辑 `portfolio.csv` 修改持仓:
```csv
symbol,name,category,alert_threshold
NVDA,NVIDIA Corporation,AI/芯片,5
TQQQ,ProShares UltraPro QQQ,杠杆ETF,5
...
```
