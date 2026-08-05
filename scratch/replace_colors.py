import re
import os

files_to_update = [
    'css/style.css',
    'index.html',
    'eventos.html'
]

# We want to replace:
# 1. CSS Variable values in style.css
# 2. Hardcoded rgba(8, 168, 142, ...) or rgba(8,168,142, ...)
# 3. Hardcoded rgba(3, 135, 187, ...) or rgba(3,135,187, ...)
# 4. Also search for any `#08a88e` or `#08A88E` or `#0387bb` or `#0387BB` and replace them

replacements = [
    # hex codes
    (re.compile(r'#08[aA]88[eE]'), '#018b48'),
    (re.compile(r'#0387[bB][bB]'), '#022966'),
    # rgba values (flexible regex to handle spaces and any opacity value)
    (re.compile(r'rgba\(\s*8\s*,\s*168\s*,\s*142\s*,\s*([^)]+)\)'), r'rgba(1, 139, 72, \1)'),
    (re.compile(r'rgba\(\s*3\s*,\s*135\s*,\s*187\s*,\s*([^)]+)\)'), r'rgba(2, 41, 102, \1)')
]

for f in files_to_update:
    path = os.path.join('c:\\Users\\USER\\Documents\\Coalizao\\sitecoalizao-main', f)
    if not os.path.exists(path):
        print(f"File {path} does not exist")
        continue
        
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        
    original = content
    for pattern, repl in replacements:
        content = pattern.sub(repl, content)
        
    if content != original:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated colors in {f}")
    else:
        print(f"No changes made in {f}")
