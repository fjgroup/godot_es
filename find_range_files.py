import os
import re

# Sections in order from getting_started to io/binary_serialization_api
# getting_started/...
# tutorials/best_practices/...
# tutorials/troubleshooting.html
# tutorials/editor/...
# tutorials/migrating/...
# tutorials/2d/...
# tutorials/3d/...
# tutorials/animation/...
# tutorials/assets_pipeline/...
# tutorials/audio/...
# tutorials/export/...
# tutorials/io/...

target_dirs = [
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
    'tutorials/io',
]
extra_files = [
    'tutorials/troubleshooting.html'
]

file_list = []
for d in target_dirs:
    if os.path.exists(d):
        for root, _, files in os.walk(d):
            for f in files:
                if f.endswith('.html'):
                    file_list.append(os.path.normpath(os.path.join(root, f)))

for ef in extra_files:
    if os.path.exists(ef):
        file_list.append(os.path.normpath(ef))

file_list = sorted(list(set(file_list)))
print(f"Total HTML files in target range: {len(file_list)}")
with open('target_file_list.txt', 'w', encoding='utf-8') as f:
    for item in file_list:
        f.write(item + '\n')
