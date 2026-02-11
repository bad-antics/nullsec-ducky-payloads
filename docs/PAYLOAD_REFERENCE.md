# Payload Reference

## Recon Payloads
| File | Target OS | Description |
|------|-----------|-------------|
| `system_info.txt` | Win/Mac/Lin | Full system enumeration |
| `wifi_survey.txt` | Win/Lin | Nearby WiFi networks |
| `network_map.txt` | Win/Lin | Local network topology |
| `installed_apps.txt` | Win/Mac | Software inventory |
| `user_enum.txt` | Win/Lin | User account enumeration |

## Exfil Payloads
| File | Target OS | Description |
|------|-----------|-------------|
| `wifi_passwords.txt` | Windows | Saved WiFi credentials |
| `browser_creds.txt` | Win/Mac | Browser saved passwords |
| `ssh_keys.txt` | Mac/Lin | SSH private key extraction |
| `discord_tokens.txt` | Win/Mac/Lin | Discord token grab |
| `clipboard_steal.txt` | Windows | Clipboard monitoring |

## Persist Payloads
| File | Target OS | Description |
|------|-----------|-------------|
| `reverse_shell.txt` | Win/Lin | Establish reverse shell |
| `scheduled_task.txt` | Windows | Scheduled task persistence |
| `cron_persist.txt` | Linux | Cron job backdoor |
| `startup_entry.txt` | Windows | Registry run key |
| `ssh_backdoor.txt` | Linux | Authorized keys injection |
