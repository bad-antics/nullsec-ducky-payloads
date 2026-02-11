# Getting Started

## Hardware Requirements

- **USB Rubber Ducky** (Hak5) — Original or Mark II
- **microSD card** — Any size (payload files are tiny)
- **SD card reader** — To transfer inject.bin

## Setup

### Step 1: Clone Payloads
```bash
git clone https://github.com/bad-antics/nullsec-ducky-payloads
cd nullsec-ducky-payloads
```

### Step 2: Choose a Payload
```bash
ls payloads/recon/       # Reconnaissance
ls payloads/exfil/       # Exfiltration
ls payloads/persist/     # Persistence
ls payloads/social/      # Social Engineering
ls payloads/utility/     # Utilities
```

### Step 3: Encode
```bash
# Hak5 DuckEncoder
java -jar duckencoder.jar -i payloads/recon/system_info.txt -o inject.bin -l us

# Or use the Python encoder
python3 ducky-encode.py payloads/recon/system_info.txt
```

### Step 4: Deploy
1. Copy `inject.bin` to Ducky's microSD
2. Insert microSD into Ducky
3. Plug Ducky into target

## Ducky Mark II

The Mark II supports DuckyScript 3.0 with extensions:
- Variables and conditionals
- Loops and functions
- Payload storage on device
- LED control and button triggers
