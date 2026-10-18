import os

dirs = [
    'getting_started',
    'tutorials/best_practices',
    'tutorials/editor',
    'tutorials/migrating',
    'tutorials/2d',
    'tutorials/3d',
    'tutorials/animation',
    'tutorials/assets_pipeline',
    'tutorials/audio',
    'tutorials/export',
    'tutorials/io'
]
en_count = 0
for d in dirs:
    for root, _, files in os.walk(d):
        for f in files:
            if f.endswith('.html'):
                p = os.path.normpath(os.path.join(root, f))
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    head = fp.read(300)
                    if 'lang="en"' in head:
                        print('Found EN:', p)
                        en_count += 1
print('Total EN in target dirs:', en_count)
