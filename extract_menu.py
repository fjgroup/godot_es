import os

with open('tutorials/io/binary_serialization_api.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

start = text.find('<div class="wy-menu wy-menu-vertical"')
end = text.find('</nav>', start)
# We want the content inside <div class="wy-menu wy-menu-vertical" ...> up to closing </div>
# In Sphinx theme:
# <div class="wy-menu wy-menu-vertical" data-spy="affix" role="navigation" aria-label="Navigation menu">
# ...
# </div>
# </div>
# </nav>

nav_part = text[start:end]
# find last </div> in nav_part
last_div = nav_part.rfind('</div>')
menu_block = nav_part[:last_div+6]
print("Menu block start:", menu_block[:100])
print("Menu block end:", menu_block[-100:])

with open('spanish_menu_sample.html', 'w', encoding='utf-8') as out:
    out.write(menu_block)
