import re
import os
import xml.etree.ElementTree as ET

text = open("README.md", encoding="utf-8").read()
refs = set(re.findall(r'(?:src|srcset)="(assets/[^"]+)"', text))
print(f"Found {len(refs)} unique asset references in README.md:")
for r in sorted(refs):
    exists = os.path.exists(r)
    status = "EXISTS" if exists else "MISSING"
    print(f"  {r}: {status}")
    if exists:
        ET.parse(r)

missing = [r for r in refs if not os.path.exists(r)]
if missing:
    print(f"ERROR: Missing files: {missing}")
else:
    print("SUCCESS: All referenced SVGs exist and are valid XML!")
