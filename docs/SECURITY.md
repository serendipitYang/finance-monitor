# 🔒 安全协议与敏感信息处理规范

**生效日期:** 2026-02-23  
**制定者:** Thomas & Zecheng  
**目的:** 保护 API keys、tokens、密码等敏感信息

---

## 🚨 核心原则

### 1. **绝不直接在聊天中发送敏感信息**
包括但不限于：
- API keys (OpenAI, Brave, GitHub, etc.)
- Access tokens
- 密码
- 私钥
- 密钥文件内容
- 完整的配置文件

### 2. **敏感信息只能存储在本地文件**
存储位置：
- `~/.openclaw/.env` - 环境变量
- `~/.openclaw/credentials.md` - 凭证记录
- `~/.openclaw/secrets/` - 密钥目录 (已添加到 .gitignore)
- 各 skill 目录下的 `.env` 文件

### 3. **只能通过文件路径告知**
正确做法：
```
✅ "Token 存储在 ~/.openclaw/github-token.md"
✅ "API key 在 ~/.openclaw/workspace/skills/stock-monitor/.env"
```

错误做法：
```
❌ "Your token is: ghp_xxxxxxxxxxxx"
❌ 发送包含 token 的截图
❌ 发送完整配置文件内容
```

---

## 👥 Telegram 用户识别

### 我能看到的信息：
- **Chat ID** (如: 8798947736) - Telegram 内部 ID
- **Sender ID** - 用户唯一标识
- **Username** (如果设置了) - 如 @username
- **First/Last name** - 显示名称

### 我**不能**看到的信息：
- **手机号** (除非用户主动提供)
- 邮箱地址
- 其他个人信息

### 当前已授权用户：
| Chat ID | 身份 | 状态 |
|---------|------|------|
| 8798947736 | Thomas (Owner) | ✅ 已授权 |
| 8711077205 | Joanna | ✅ 已授权 |

---

## 🛡️ Telegram 访问控制

### 当前配置问题：
```json
{
  "dmPolicy": "open",  // ❌ 任何人可以发私信
  "allowFrom": ["*"]   // ❌ 允许所有人
}
```

### 建议的安全配置：
```bash
# 1. 限制为仅允许列表中的用户
openclaw config set channels.telegram.dmPolicy allowlist

# 2. 添加授权用户 (你、Joanna)
openclaw config set channels.telegram.allowFrom '["8798947736", "8711077205"]'

# 3. 重启 Gateway 生效
openclaw gateway restart
```

---

## 📋 敏感信息处理检查清单

### 当我需要处理敏感信息时：
- [ ] 不直接在回复中包含明文 token
- [ ] 不发送包含敏感信息的截图
- [ ] 只提供本地文件路径
- [ ] 确认信息不会进入 git 历史
- [ ] 使用 `.gitignore` 保护敏感文件

### 示例场景：

**场景 1: GitHub Token**
```
用户: 我的 GitHub token 是什么？

❌ 错误回复:
"ghp_xxxxxxxxxxxx..."

✅ 正确回复:
"Token 存储在 ~/.openclaw/github-token.md"
```

**场景 2: API Key**
```
用户: 我的 Brave API key 在哪里？

❌ 错误回复:
"BSArk_2E4xNkSe3qL3Bsrx9efxIry5Q"

✅ 正确回复:
"Brave API key 在 ~/.openclaw/config.yaml 中，查看 brave.apiKey 字段"
```

**场景 3: 需要 Token 进行操作**
```
用户: 配置一下 OpenAI API

❌ 错误做法:
直接在对话中发送 API key

✅ 正确做法:
"请创建文件 ~/.openclaw/.env，写入 OPENAI_API_KEY=your_key_here，我会读取该文件"
```

---

## 🔐 文件安全分类

### 🔴 绝密 (绝不进入 git)
- `~/.openclaw/.env` - 环境变量
- `~/.openclaw/*-token.md` - 各种 tokens
- `~/.openclaw/credentials.md` - 密码记录
- `*/.env` - 各 skill 的环境文件

### 🟡 敏感 (可能包含配置信息)
- `~/.openclaw/config.yaml` - OpenClaw 配置
- `~/.openclaw/openclaw.json` - Gateway 配置

### 🟢 安全 (可以 git 跟踪)
- `SOUL.md`, `AGENTS.md` - 配置文件
- `skills/*/SKILL.md` - Skill 文档
- 脚本代码

---

## 📝 事故响应

### 如果敏感信息意外泄露：
1. **立即撤销 token** - 在服务商处重置
2. **从对话历史中删除** - 如果平台支持
3. **更新安全协议** - 防止再次发生
4. **通知 Thomas** - 说明情况

---

## ✅ 已实施的措施

- [x] `.gitignore` 已配置保护敏感文件
- [x] 凭证存储在本地文件
- [x] GitHub Token 已从 git 历史中移除
- [ ] Telegram 访问控制 (待配置)
- [ ] 定期安全审查 (建议每月)

---

## 🔧 待执行任务

### 立即执行 (由 Thomas 决定)
1. **配置 Telegram 访问限制**
   ```bash
   openclaw config set channels.telegram.dmPolicy allowlist
   openclaw config set channels.telegram.allowFrom '["8798947736", "8711077205"]'
   openclaw gateway restart
   ```

2. **验证安全措施**
   - 测试第三方无法发送消息
   - 确认 Joanna 可以正常对话

### 定期维护
- 每月审查授权的 Telegram 用户
- 检查是否有敏感信息意外提交到 git
- 更新过期的 tokens

---

**最后更新:** 2026-02-23  
**下次审查:** 2026-03-23
