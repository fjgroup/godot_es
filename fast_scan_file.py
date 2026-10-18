import os
import re

with open('target_file_list.txt', 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

out_lines = []

for idx, p in enumerate(files):
    try:
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            content = fp.read()
    except Exception as e:
        continue
    
    # Check title / H1
    h1_m = re.search(r'<h1>(.*?)</h1>', content)
    h1 = ""
    if h1_m:
        h1 = re.sub(r'<[^>]+>', '', h1_m.group(1)).strip()
    
    # Extract articleBody
    body_idx = content.find('<div itemprop="articleBody">')
    footer_idx = content.find('<footer>', body_idx) if body_idx != -1 else -1
    body = content[body_idx:footer_idx] if body_idx != -1 and footer_idx != -1 else ""
    
    plain_text = re.sub(r'<[^>]+>', ' ', body)
    
    # Find english headings
    en_headings = re.findall(r'<h[1-4][^>]*>([^<]*(?:Introduction|Contents|Overview|Prerequisites|Summary|Description|Before you start)[^<]*)</h[1-4]>', body, re.I)
    
    en_matches = len(re.findall(r'\b(the|and|this|with|from|which|when|that|into|about)\b', plain_text, re.I))
    es_matches = len(re.findall(r'\b(el|la|los|las|este|esta|estos|estas|para|como|cuando)\b', plain_text, re.I))
    
    # Check if body has English sections
    is_mostly_en = en_matches > 30 and (en_matches / (en_matches + es_matches + 1)) > 0.4
    has_en_headings = len(en_headings) > 0
    has_io_header = '<h1>File and data I/O' in content or '<h1>File and data I/O' in body
    
    if is_mostly_en or has_en_headings or has_io_header:
        out_lines.append(f"{p} | mostly_en={is_mostly_en} (EN:{en_matches}/ES:{es_matches}) | headings={en_headings[:2]} | h1={h1}")

with open('scan_results.txt', 'w', encoding='utf-8') as out:
    for line in out_lines:
        out.write(line + '\n')

print(f"Done! {len(out_lines)} flagged out of {len(files)} files.")
