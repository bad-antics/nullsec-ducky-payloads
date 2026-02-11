# Troubleshooting

## Payload doesn't execute

- **Check encoding**: Re-encode with correct keyboard layout
- **Add more delays**: Slow systems need longer `DELAY` values
- **USB recognition**: Some systems take 3-5 seconds to recognize HID
- **Try different port**: Front panel USB may have lower priority

## Wrong characters typed

- **Keyboard layout mismatch**: Encode with matching layout flag
  ```bash
  # For US layout
  java -jar duckencoder.jar -i payload.txt -o inject.bin -l us
  
  # For UK layout
  java -jar duckencoder.jar -i payload.txt -o inject.bin -l gb
  ```

## PowerShell execution policy blocks

Add this at the start of PowerShell payloads:
```duckyscript
STRING Set-ExecutionPolicy Bypass -Scope Process -Force
ENTER
DELAY 500
```

## macOS security blocks

Modern macOS blocks keyboard input to Terminal by default. Workaround:
```duckyscript
REM Use Spotlight instead
GUI SPACE
DELAY 500
STRING terminal
DELAY 500
ENTER
DELAY 1500
REM macOS will prompt for accessibility permission
```
