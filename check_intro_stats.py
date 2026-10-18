import os
import re

files = [
    'getting_started/introduction/first_look_at_the_editor.html',
    'getting_started/introduction/godot_design_philosophy.html',
    'getting_started/introduction/index.html',
    'getting_started/introduction/introduction_to_godot.html',
    'getting_started/introduction/key_concepts_overview.html',
    'getting_started/introduction/learning_new_features.html',
    'getting_started/introduction/learn_to_code_with_gdscript.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    b_start = c.find('<div itemprop="articleBody">')
    b_end = c.find('<footer>', b_start)
    body = c[b_start:b_end]
    plain = re.sub(r'<[^>]+>', ' ', body)
    en = len(re.findall(r'\b(the|and|is|in|to|of|with|for|you|this|that)\b', plain, re.I))
    es = len(re.findall(r'\b(el|la|los|las|de|en|un|una|para|con|por|este|esta)\b', plain, re.I))
    print(f"{p}: EN={en}, ES={es}")
