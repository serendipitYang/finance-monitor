#!/usr/bin/env python3
"""
Finance News and Stock Monitor for Thomas
Simplified version using yfinance directly
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import json
import sys
import os

# Thomas's portfolio
PORTFOLIO = {
    "NVDA": {"name": "NVIDIA", "category": "AI/芯片"},
    "TQQQ": {"name": "ProShares UltraPro QQQ", "category": "杠杆ETF"},
    "MU": {"name": "Micron", "category": "存储芯片"},
    "FIG": {"name": "FIG", "category": "待确认"},
    "KLAR": {"name": "KLAR", "category": "待确认"},
    "AIRO": {"name": "AIRO", "category": "待确认"},
    "RVI": {"name": "RVI", "category": "待确认"},
    "BTC-USD": {"name": "Bitcoin", "category": "加密货币"},
}

def get_stock_price(symbol):
    """Get current stock price and daily change"""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="2d")
        if len(hist) >= 2:
            current = hist['Close'].iloc[-1]
            previous = hist['Close'].iloc[-2]
            change = ((current - previous) / previous) * 100
            return {
                "price": round(current, 2),
                "change": round(change, 2),
                "volume": int(hist['Volume'].iloc[-1])
            }
    except Exception as e:
        return {"error": str(e)}
    return None

def generate_briefing():
    """Generate daily market briefing"""
    print("📊 早安简报 - " + datetime.now().strftime("%Y-%m-%d"))
    print()
    
    # Market overview
    print("全球市场:")
    indices = {
        "^GSPC": "S&P 500",
        "^IXIC": "NASDAQ",
        "^DJI": "DOW"
    }
    
    for symbol, name in indices.items():
        data = get_stock_price(symbol)
        if data and "error" not in data:
            emoji = "🟢" if data['change'] > 0 else "🔴"
            print(f"{emoji} {name}: {data['change']:+.2f}%")
    print()
    
    # Portfolio
    print("持仓动态:")
    for symbol, info in PORTFOLIO.items():
        data = get_stock_price(symbol)
        if data and "error" not in data:
            emoji = "🟢" if data['change'] > 0 else "🔴"
            print(f"{emoji} {symbol}: {data['change']:+.2f}% (${data['price']})")
    print()
    
    print("今日关注:")
    print("• NVDA 财报预期")
    print("• 美联储利率决定")

def check_alerts():
    """Check for price alerts"""
    alerts = []
    for symbol, info in PORTFOLIO.items():
        data = get_stock_price(symbol)
        if data and "error" not in data:
            if abs(data['change']) > 5:
                alerts.append({
                    "symbol": symbol,
                    "change": data['change'],
                    "price": data['price']
                })
    return alerts

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--briefing":
            generate_briefing()
        elif sys.argv[1] == "--alerts":
            alerts = check_alerts()
            if alerts:
                print("🚨 价格警报:")
                for alert in alerts:
                    emoji = "🟢" if alert['change'] > 0 else "🔴"
                    print(f"{emoji} {alert['symbol']}: {alert['change']:+.2f}% (${alert['price']})")
            else:
                print("✅ 无异常波动")
        else:
            print("Usage: python finance_monitor.py [--briefing|--alerts]")
    else:
        generate_briefing()

if __name__ == "__main__":
    main()
