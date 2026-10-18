import os
import re

with open('getting_started/introduction/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'<div class="wy-menu wy-menu-vertical"[^>]*>(.*?)</div>\s*</div>\s*</nav>', text, re.DOTALL)
if m:
    nav = m.group(1)
    # find manual section
    manual_m = re.search(r'(<p class="caption"[^>]*><span class="caption-text">Manual</span></p>.*?)(<p class="caption"|$)', nav, re.DOTALL)
    if manual_m:
        print("MANUAL IN ES DOCS:")
        # print first 50 lines of manual
        lines = manual_m.group(1).splitlines()[:50]
        for l in lines:
            print(l)
else:
    print("Nav not found")
