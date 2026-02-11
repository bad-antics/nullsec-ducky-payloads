# Installation

## Clone Repository
```bash
git clone https://github.com/bad-antics/nullsec-ducky-payloads.git
cd nullsec-ducky-payloads
```

## Encoder Setup

### Java DuckEncoder (Official)
```bash
wget https://github.com/hak5/usbrubberducky-payloads/raw/master/duckencoder.jar
java -jar duckencoder.jar -i payload.txt -o inject.bin
```

### Python Alternative
```bash
pip install ducky-tools
ducky-encode payload.txt -o inject.bin
```

## Deploy to Ducky
1. Insert Ducky's microSD into your computer
2. Copy `inject.bin` to the root of the SD card
3. Eject SD card and insert into Ducky
4. Plug Ducky into target
