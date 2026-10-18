import os

en_files = []
es_files = []
other_files = []

for root, _, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.normpath(os.path.join(root, f))
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    head = fp.read(400)
                    if 'lang="en"' in head:
                        en_files.append(p)
                    elif 'lang="es"' in head:
                        es_files.append(p)
                    else:
                        other_files.append(p)
            except Exception:
                pass

print(f"Total HTML files: {len(en_files) + len(es_files) + len(other_files)}")
print(f"lang=en files: {len(en_files)}")
print(f"lang=es files: {len(es_files)}")
print(f"other files: {len(other_files)}")

with open('en_html_files.txt', 'w', encoding='utf-8') as out:
    for ef in sorted(en_files):
        out.write(ef + '\n')
