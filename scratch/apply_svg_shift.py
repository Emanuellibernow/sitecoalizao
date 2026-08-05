import re
import colorsys
import os

svg_path = 'images/hero-coalizao-fluid-detailed.svg'
if not os.path.exists(svg_path):
    print("SVG file not found!")
    exit(1)

with open(svg_path, 'r', encoding='utf-8') as f:
    content = f.read()

def shift_color_match(match):
    hex_str = match.group(0).lstrip('#')
    r = int(hex_str[0:2], 16) / 255.0
    g = int(hex_str[2:4], 16) / 255.0
    b = int(hex_str[4:6], 16) / 255.0
    
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h_deg = h * 360.0
    
    if 140 <= h_deg <= 210:
        h_deg_new = 155.0 + (h_deg - 170.0) * 0.6
        h_new = h_deg_new / 360.0
        s_new = min(1.0, max(0.0, s * (0.82 / 0.91)))
        l_new = min(1.0, max(0.0, l * (0.31 / 0.35)))
        r_new, g_new, b_new = colorsys.hls_to_rgb(h_new, l_new, s_new)
        return '#{:02x}{:02x}{:02x}'.format(int(r_new * 255 + 0.5), int(g_new * 255 + 0.5), int(b_new * 255 + 0.5))
    return '#' + hex_str

# Find all hex colors in the SVG and replace them using our HSL function
hex_pattern = re.compile(r'#[0-9a-fA-F]{6}')
new_content = hex_pattern.sub(shift_color_match, content)

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully shifted colors in images/hero-coalizao-fluid-detailed.svg")
