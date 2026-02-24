# 🔧 Browser 工具稳定性问题 - 调研报告

**日期:** 2026-02-23  
**问题:** Browser 工具不稳定，经常出现 "tab not found" 和 "Chrome extension relay" 错误

---

## 🔍 发现的相关 GitHub Issues

### 1. Issue #1998 - "tab not found when multiple tabs have same URL"
**状态:** Open  
**根本原因:**
- Playwright 的 `newCDPSession(page)` 尝试使用 `Target.attachToBrowserTarget` 创建 CDP session
- Chrome 的 extension debugger API 不支持此方法，返回 `{"code":-32000,"message":"Not allowed"}`
- 导致 `findPageByTargetId()` 失败，返回 "tab not found"

### 2. Issue #9723 - "browser.snapshot ignores profile parameter"
**状态:** Open (HIGH severity)  
**问题:**
- `browser.snapshot` 总是使用 Chrome extension relay (port 18792)
- 忽略 `profile="openclaw"` 参数
- 即使使用 `openclaw` profile 打开页面，snapshot 仍尝试连接 extension relay

### 3. Issue #1160 - "Browser Relay loses connection after tab switch"
**状态:** Open  
**根本原因:**
- `chrome.debugger detach/reattach` 处理不当
- 切换 tab 后连接丢失

### 4. Issue #8146 - "browser tool interaction failing"
**状态:** Open  
**描述:** 即使使用 `openclaw` profile 也出现 timeout/extension relay 错误

---

## 🐛 问题根本原因

```
┌─────────────────────────────────────────────────────────┐
│  Browser 工具架构问题                                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Profile 参数被忽略                                    │
│     - snapshot 总是使用 extension relay (18792)          │
│     - 忽略 openclaw profile (18800)                      │
│                                                         │
│  2. Chrome Extension API 限制                            │
│     - 不支持 Target.attachToBrowserTarget               │
│     - CDP session 创建失败                              │
│                                                         │
│  3. Tab ID 匹配失败                                       │
│     - Playwright 无法通过 targetId 找到 page             │
│     - 导致 "tab not found" 错误                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## ✅ 推荐的解决方案

### 方案 1: 使用纯 CDP (推荐) - 绕过 Extension Relay

**原理:** 直接使用 Chrome DevTools Protocol，不通过 extension

**实现:**
```javascript
// 启动 Chrome 时指定 remote-debugging-port
chrome --remote-debugging-port=9222

// 然后使用 CDP 直接连接
const cdpUrl = 'http://127.0.0.1:9222';
```

**优点:**
- 绕过 extension relay 的所有问题
- 稳定，不受 extension 状态影响
- 支持所有 CDP 功能

**缺点:**
- 需要手动启动 Chrome
- 需要指定固定的 debugging port

---

### 方案 2: 使用 Playwright 直接 (推荐)

**原理:** 绕过 OpenClaw browser tool，直接使用 Playwright

**实现:**
```python
# Python script using Playwright directly
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="screenshot.png")
```

**优点:**
- 完全控制浏览器
- 稳定可靠
- 不依赖 OpenClaw browser tool

**缺点:**
- 需要额外编写脚本
- 不集成到 OpenClaw workflow

---

### 方案 3: 使用 Selenium / Puppeteer

**原理:** 使用其他浏览器自动化工具

**优点:**
- 成熟稳定
- 社区支持好

**缺点:**
- 需要额外安装
- 学习曲线

---

### 方案 4: 等待 OpenClaw 官方修复

**相关 PR:**
- 需要修复 `browser.snapshot` 的 profile 参数处理
- 需要修复 CDP session 创建失败的问题

**时间:** 不确定

---

## 🚀 立即可用的 Workaround

### 方法 A: 使用 curl 直接访问 CDP

```bash
# 获取页面列表
curl http://127.0.0.1:18800/json/list

# 截图 (需要页面支持)
curl -X POST -d '{"id":1,"method":"Page.captureScreenshot"}' \
  http://127.0.0.1:18800/json
```

### 方法 B: 使用 Python + Playwright

已安装到 `skills/stock-monitor/` 目录，可以参考：
- `playwright_script.py` - 直接使用 Playwright

### 方法 C: 使用 `openclaw` profile 但避免 snapshot

```javascript
// 只使用 open 和 navigate，避免 snapshot
browser.open({ profile: "openclaw", targetUrl: "..." })
// 然后使用 web_fetch 获取内容
```

---

## 📝 建议的下一步

### 短期 (今天)
1. ✅ 使用 web_search + web_fetch 替代 browser (已完成)
2. ✅ 使用 Python + Playwright 脚本 (已配置)

### 中期 (本周)
3. 编写通用的 Playwright 自动化脚本
4. 封装成 OpenClaw skill

### 长期 (等待官方)
5. 关注 GitHub issues #1998, #9723
6. 升级 OpenClaw 到修复版本

---

## 📊 当前状态

| 方案 | 状态 | 可行性 |
|------|------|--------|
| OpenClaw browser tool | ⚠️ 不稳定 | 需要修复 |
| CDP direct (curl) | ✅ 可用 | 需要手动 |
| Playwright direct | ✅ 已配置 | 推荐 |
| Selenium | ⏳ 待配置 | 备选 |

---

## 🔗 参考链接

- Issue #1998: https://github.com/openclaw/openclaw/issues/1998
- Issue #9723: https://github.com/openclaw/openclaw/issues/9723
- Issue #1160: https://github.com/openclaw/openclaw/issues/1160
- Issue #8146: https://github.com/openclaw/openclaw/issues/8146

---

*报告生成: 2026-02-23*  
*建议: 使用 Playwright direct 方案绕过当前限制*
