import os
import re

with open('getting_started/introduction/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

m = re.search(r'<div class="wy-menu wy-menu-vertical"[^>]*>(.*?)</div>\s*</div>\s*</nav>', text, re.DOTALL)
nav = m.group(1)

# Find toctree-l1 entries in Manual
manual_m = re.search(r'<p class="caption"[^>]*><span class="caption-text">Manual</span></p>\s*<ul>(.*?)</ul>\s*<p class="caption"', nav, re.DOTALL)
if manual_m:
    manual_content = manual_m.group(1)
    l1s = re.findall(r'<li class="toctree-l1"><a class="reference internal" href="([^"]+)">([^<]+)</a>', manual_content)
    print(f"Found {len(l1s)} L1 sections in Manual:")
    for href, title in l1s:
        print(f"  {title.strip()}: {href}")
else:
    print("Manual not matched cleanly")
