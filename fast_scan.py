import os
import re

with open('target_file_list.txt', 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

print(f"Checking {len(files)} files...")

results = []
for idx, p in enumerate(files):
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
    except Exception as e:
        continue
    
    # Check title / H1
    h1_m = re.search(r'<h1>(.*?)</h1>', content)
    h1 = h1_m.group(1).strip() if h1_m else ""
    
    # Check if 'File and data I/O' is in title or breadcrumbs
    io_in_file = 'File and data I/O' in content
    
    # Extract articleBody
    body_idx = content.find('<div itemprop="articleBody">')
    footer_idx = content.find('<footer>', body_idx) if body_idx != -1 else -1
    
    body = content[body_idx:footer_idx] if body_idx != -1 and footer_idx != -1 else ""
    
    # Find English headings in body
    en_headings = re.findall(r'<h[1-4][^>]*>([^<]*(?:Introduction|Contents|Overview|Prerequisites|Summary|Description|Before you start)[^<]*)</h[1-4]>', body, re.I)
    
    # Check english words in body
    # sample some text
    plain_text = re.sub(r'<[^>]+>', ' ', body)
    words = plain_text.split()
    total_words = len(words)
    
    en_matches = len(re.findall(r'\b(the|and|this|with|from|which|when|that|into|about)\b', plain_text, re.I))
    es_matches = len(re.findall(r'\b(el|la|los|las|este|esta|estos|estas|para|como|cuando)\b', plain_text, re.I))
    
    if en_matches > 30 and (en_matches / (en_matches + es_matches + 1)) > 0.4:
        results.append((p, f"Mostly English text (EN:{en_matches}, ES:{es_matches})", h1))
    elif en_headings:
        results.append((p, f"English headings: {en_headings[:3]}", h1))
    elif io_in_file:
        results.append((p, "Contains 'File and data I/O'", h1))

print(f"Total files flagged: {len(results)}")
for r in results:
    print(f"{r[0]} | {r[1]} | {r[2]}")
