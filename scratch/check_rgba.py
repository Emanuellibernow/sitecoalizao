import re

files = ['index.html', 'eventos.html', 'css/style.css']

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.readlines()
    for idx, line in enumerate(content):
        if '8, 168, 142' in line or '8,168,142' in line:
            print(f"{f}:L{idx+1} (teal RGBA): {line.strip()}")
        if '3, 135, 187' in line or '3,135,187' in line:
            print(f"{f}:L{idx+1} (blue RGBA): {line.strip()}")
