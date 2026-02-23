# 开发环境配置记录

**日期:** 2026-02-23  
**配置者:** Thomas 授权，Zecheng 执行

---

## ✅ 已完成配置

### 1. Miniconda + Python 环境

**安装:**
```bash
brew install miniconda
```

**版本:**
- conda 25.11.1
- Python 3.11 (finance 环境)

**激活方式:**
```bash
eval "$(/opt/homebrew/bin/conda shell.zsh hook)"
conda activate finance
```

**已安装包:**
- yfinance (股票数据)
- pandas (数据处理)
- numpy (数值计算)
- requests (HTTP 请求)
- python-dotenv (环境变量)

### 2. Sub-Agent 配置

**路径:** `~/.openclaw/agents/`

| Agent | 模型 | 用途 |
|-------|------|------|
| researcher | Claude Sonnet 4.6 | 深度调研 |
| coder | Claude Sonnet 4.6 | 代码/脚本 |
| browser-operator | Claude Sonnet 4.6 | 浏览器自动化 |

**配置特点:**
- `coder` 使用 `thinking: high` (复杂代码任务)
- `timeout: 600s` (给足时间)
- 所有工具已启用

### 3. Git 配置

```bash
git config --global user.name "Thomas Yang"
git config --global user.email "yhan65905@gmail.com"
git config --global init.defaultBranch main
```

### 4. GitHub CLI

```bash
brew install gh
gh version 2.87.2
```

**状态:** 已安装，待认证

---

## ⏳ 待完成

### Docker
- 已安装但需手动启动 Desktop
- 启动命令: `open -a Docker`
- 首次启动需配置

### GitHub 认证
**方案:** 等待 Thomas 提供方案
- A: 手动创建 repo 后给我 URL
- B: 提供 Personal Access Token
- C: 稍后处理

---

## 🚀 快速测试

### 激活环境
```bash
eval "$(/opt/homebrew/bin/conda shell.zsh hook)"
conda activate finance
```

### 运行监控脚本
```bash
python ~/.openclaw/workspace/skills/stock-monitor/stock_monitor.py --briefing
```

### 检查持仓
```bash
cat ~/.openclaw/workspace/memory/data/portfolio.csv
```

---

## 📝 文件位置

```
~/.openclaw/
├── agents/
│   ├── researcher.json
│   ├── coder.json
│   └── browser-operator.json
├── workspace/
│   └── skills/
│       └── stock-monitor/
│           ├── stock_monitor.py
│           └── SKILL.md
└── miniconda3/ (conda 安装目录)
```

---

## 🔧 常用命令

```bash
# 激活环境
conda activate finance

# 退出环境
conda deactivate

# 安装包
pip install <package>

# 查看已安装包
pip list

# GitHub CLI 登录 (待完成)
gh auth login

# Docker 启动
open -a Docker
```

---

*下次更新: GitHub 配置完成后*
