# NullSec Ducky Payloads Wiki

Welcome to the **NullSec Ducky Payloads** wiki — 50+ USB Rubber Ducky payloads for security research.

## Navigation

- [[Getting Started]] — Setup your Rubber Ducky
- [[Payload Categories]] — Browse all payloads
- [[Writing Payloads]] — Create custom DuckyScript
- [[Encoding Guide]] — Encode payloads for injection
- [[OS Targets]] — Windows, macOS, Linux specifics
- [[Troubleshooting]] — Fix common issues

## Categories

| Category | Count | Description |
|----------|------:|-------------|
| 🔍 Recon | 10 | System enumeration |
| 📤 Exfil | 10 | Data extraction |
| 🔐 Persist | 10 | Backdoor installation |
| 🎭 Social | 10 | Social engineering |
| 🛠️ Utility | 10 | Admin tools |

## Quick Start

1. Write or select a payload `.txt` file
2. Encode it: `java -jar duckencoder.jar -i payload.txt -o inject.bin`
3. Copy `inject.bin` to Ducky microSD
4. Insert Ducky into target USB port
