from nullsec_ducky_payloads.core import DuckyScriptBuilder,PayloadLibrary
d=DuckyScriptBuilder()
payload=d.build_script(["DELAY 1000","GUI r","DELAY 500","STRING notepad","ENTER","DELAY 1000","STRING Hello from Rubber Ducky!","ENTER"])
print("DuckyScript:")
print(payload)
l=PayloadLibrary()
print(f"\nPayload categories: {list(l.list_payloads().keys())}")
print(f"Total payloads: {l.count()}")
