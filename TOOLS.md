# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## Emei Peak (Mac mini)

- **Hostname:** Emei-Peaks-Mac-mini.local
- **IP:** 10.0.0.214 (Tailscale enabled)
- **Access:** Screen Sharing (VNC) + SSH
- **Status:** Headless setup — no monitor/keyboard needed

### Remote Access

| Method | Address/Link | Notes |
|--------|-------------|-------|
| **Parsec** | https://parsec.gg/g/3A3YiWwfMY3NsEJngsrzh6wNdJi/ab19ebb1/ | ⭐ 推荐，低延迟，适合 Joanna |
| **Tailscale SSH** | `ssh emei_peak@100.120.109.51` | 命令行访问 |
| **Screen Sharing** | `vnc://100.120.109.51` | 原生 macOS |
| **AirPlay** | Emei-Peaks-Mac-mini | 同一 WiFi 可用 |
| **OpenClaw** | http://Emei-Peaks-Mac-mini.local:18789/ | 管理面板 |

### Channels

- **Telegram:** @EmeiPeak_bot → Thomas (ID: 8798947736)
- **Control UI:** Local web dashboard when on same network

### Users

| User | Purpose | Access |
|------|---------|--------|
| **Zecheng (Emei Peak)** | AI assistant, automation, background tasks | Always-on, headless |
| **Joanna** | Remote work, Chrome sessions, interactive tasks | Remote Desktop / Screen Sharing |
| **Thomas (Boss)** | Admin, owner, full access | SSH, Screen Sharing, Telegram |

### Chrome Profiles

- Profile 1: **Zecheng** — for automation, research, agent tasks
- Profile 2: **Joanna** — for work sessions, separate login

Note: Each user should use their own Chrome profile to keep sessions isolated.

---

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
