<div align="center">

```
 ██████╗ ██╗   ██╗ ██████╗██╗  ██╗██╗   ██╗    ██████╗  █████╗ ██╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗
 ██╔══██╗██║   ██║██╔════╝██║ ██╔╝╚██╗ ██╔╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝
 ██║  ██║██║   ██║██║     █████╔╝  ╚████╔╝     ██████╔╝███████║ ╚████╔╝ ██║     ██║   ██║███████║██║  ██║███████╗
 ██║  ██║██║   ██║██║     ██╔═██╗   ╚██╔╝      ██╔═══╝ ██╔══██║  ╚██╔╝  ██║     ██║   ██║██╔══██║██║  ██║╚════██║
 ██████╔╝╚██████╔╝╚██████╗██║  ██╗   ██║       ██║     ██║  ██║   ██║   ███████╗╚██████╔╝██║  ██║██████╔╝███████║
 ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
                       [ RUBBER DUCKY BADUSB PAYLOADS | bad-antics ]
```

### 🦆 USB Rubber Ducky Payloads for Security Research

[![GitHub](https://img.shields.io/badge/GitHub-bad--antics-181717?style=for-the-badge&logo=github)](https://github.com/bad-antics)
[![Hak5](https://img.shields.io/badge/Hak5-Ducky-FF6B35?style=for-the-badge)](https://hak5.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## ⚠️ Disclaimer

**FOR AUTHORIZED SECURITY TESTING ONLY.** These payloads are for legitimate penetration testing with proper authorization. Unauthorized use is illegal.

---

## 🦆 Payloads

### 🪟 Windows

| Payload | Description |
|---------|-------------|
| `wifi-exfil.txt` | Extract saved WiFi credentials |
| `reverse-shell.txt` | PowerShell reverse shell |
| `system-recon.txt` | System info gathering |
| `disable-defender.txt` | Disable Windows Defender |
| `persistence.txt` | Establish persistence |

### 🍎 macOS

| Payload | Description |
|---------|-------------|
| `keychain-dump.txt` | Keychain credential extraction |
| `shell-spawn.txt` | Spawn reverse shell |
| `browser-creds.txt` | Browser credential grab |

### 🐧 Linux

| Payload | Description |
|---------|-------------|
| `shadow-grab.txt` | Extract /etc/shadow |
| `ssh-keys.txt` | SSH key exfiltration |
| `netcat-shell.txt` | Netcat reverse shell |

---

## 🚀 Usage

1. **Encode payload** using Hak5 Payload Studio
2. **Load onto Ducky** via SD card
3. **Insert into target** (with authorization!)
4. **Payload executes** automatically

---

## 📝 Payload Format

```ducky
REM WiFi Credential Extraction
DELAY 1000
GUI r
DELAY 500
STRING powershell -w hidden
ENTER
DELAY 1000
STRING netsh wlan export profile key=clear
ENTER
```

---

## 🔗 NullSec Hak5 Suite

| Repo | Description |
|------|-------------|
| **[Ducky Payloads](https://github.com/bad-antics/nullsec-ducky-payloads)** | Rubber Ducky (you are here) |
| **[Bunny Payloads](https://github.com/bad-antics/nullsec-bunny-payloads)** | Bash Bunny attacks |
| **[Flipper Suite](https://github.com/bad-antics/nullsec-flipper-suite)** | Flipper Zero tools |

---

<div align="center">

**[GitHub](https://github.com/bad-antics)** • **[NullSec](https://github.com/bad-antics/nullsec)** • **[Issues](https://github.com/bad-antics/nullsec-ducky-payloads/issues)**

*Part of the NullSec Framework*

</div>
