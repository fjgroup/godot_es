import os
import re

with open('target_file_list.txt', 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

# Common English headings / admonitions / phrases to check in body
patterns = [
    r'<div class="admonition attention latest-notice">.*?<p class="first admonition-title">Attention: Here be dragons</p>',
    r'<h\d[^>]*>(?:Contents|Overview|Introduction|Description|Tutorials|Properties|Methods|Prerequisites|Summary)</h\d>',
    r'File and data I/O',
]

results = []
for p in files:
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
    except Exception as e:
        continue
    
    # extract articleBody or main section
    body_m = re.search(r'<div itemprop="articleBody">(.*?)</div>\s*<footer>', content, re.DOTALL)
    if not body_m:
        body_m = re.search(r'<div role="main"[^>]*>(.*?)</div>\s*<footer>', content, re.DOTALL)
    
    if body_m:
        body = body_m.group(1)
        # Check title
        title_m = re.search(r'<h1>(.*?)</h1>', body)
        h1 = title_m.group(1) if title_m else ""
        
        # Check for English paragraphs or sections
        # Count some common English indicators in body
        en_words = len(re.findall(r'\b(the|and|is|in|to|of|with|for|you|this|that)\b', body, re.IGNORECASE))
        es_words = len(re.findall(r'\b(el|la|los|las|de|en|un|una|para|con|por|este|esta)\b', body, re.IGNORECASE))
        
        ratio = en_words / (en_words + es_words + 1)
        if ratio > 0.35 and en_words > 30:
            results.append((p, f"Mostly English (EN:{en_words}, ES:{es_words})", h1))
        elif 'File and data I/O' in body:
            results.append((p, "Contains 'File and data I/O'", h1))
        elif re.search(r'<h2>(?:Introduction|Overview|Contents|Summary|Prerequisites)</h2>', body, re.I):
            results.append((p, "Contains English H2", h1))

print(f"Files needing translation attention: {len(results)}")
for r in results:
    print(r)
