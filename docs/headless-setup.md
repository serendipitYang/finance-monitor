# Headless Mac Mini Setup

## Status
✅ SSH Enabled — `ssh emei_peak@Emei-Peaks-Mac-mini.local`
✅ Screen Sharing Enabled — `vnc://Emei-Peaks-Mac-mini.local`
✅ OpenClaw Gateway Running — `http://Emei-Peaks-Mac-mini.local:18789/`
✅ Telegram Connected — @EmeiPeak_bot
✅ Tailscale Enabled — Remote access from anywhere

## Pre-Disconnect Checklist

- [x] Remote Login (SSH) — ON
- [x] Screen Sharing (VNC) — ON
- [x] OpenClaw auto-starts on boot
- [x] User `emei_peak` auto-login configured
- [x] WiFi credentials saved
- [x] Power settings: Never sleep on AC

## Access Methods

### From Same Network (MacBook Pro)

1. **Screen Sharing:**
   - Finder → Go → Connect to Server
   - `vnc://Emei-Peaks-Mac-mini.local`
   - Or open Safari and click `vnc://Emei-Peaks-Mac-mini.local`

2. **SSH:**
   ```bash
   ssh emei_peak@Emei-Peaks-Mac-mini.local
   ```

### From Anywhere (Tailscale)

```bash
# Tailscale IP (check with `tailscale ip`)
ssh emei_peak@<tailscale-ip>
```

## Post-Disconnect Actions

Once monitor is disconnected, I will:

1. Run `pmset` to prevent sleep on AC power
2. Verify OpenClaw health status
3. Test remote connectivity
4. Confirm Joanna can connect via Screen Sharing

## Troubleshooting

**If you can't connect:**
- Check Mac mini is powered on (LED on)
- Verify same WiFi network (local access)
- Try Tailscale IP instead of .local hostname
- Restart from OpenClaw dashboard if needed

**If I "go offline":**
- Mac probably went to sleep — need to adjust power settings
- WiFi may have disconnected
- OpenClaw service may need restart
