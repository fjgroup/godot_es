import os
import re

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

captions = re.findall(r'<p class="caption"[^>]*>.*?</p>', text, re.DOTALL)
print("CAPTIONS IN INDEX.HTML:")
for c in captions:
    print(c.strip())

# Check tutorials/io/binary_serialization_api.html
with open('tutorials/io/binary_serialization_api.html', 'r', encoding='utf-8', errors='ignore') as f:
    text2 = f.read()

captions2 = re.findall(r'<p class="caption"[^>]*>.*?</p>', text2, re.DOTALL)
print("\nCAPTIONS IN BINARY SERIALIZATION:")
for c in captions2:
    print(c.strip())
