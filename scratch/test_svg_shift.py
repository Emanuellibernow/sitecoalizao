import colorsys

colors_in_svg = ['#36BFA7', '#43C7B1', '#47C8B2', '#4AC9B3', '#69D9C5', '#6EDAC8', '#72DCC7', '#76DEC9', '#77DEC9', '#7BE2CE', '#7DDFC9', '#83E5D5', '#86E6D4', '#8FE9DB', '#91EBDD', '#96EDE0', '#9BECDD', '#9FEFE3', '#A6EFE1', '#AAF3E8', '#B0F2E5', '#B6F3E8', '#B9F4E8', '#BAF5EA', '#C5F8EF', '#C7F7EE', '#D9FBF4', '#E6FFF9', '#E8FFF9', '#F1FFFC']

def shift_color(hex_str):
    hex_str = hex_str.lstrip('#')
    r = int(hex_str[0:2], 16) / 255.0
    g = int(hex_str[2:4], 16) / 255.0
    b = int(hex_str[4:6], 16) / 255.0
    
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h_deg = h * 360.0
    
    # We want to shift all cyan/teal colors (H between 140 and 210)
    if 140 <= h_deg <= 210:
        h_deg_new = 155.0 + (h_deg - 170.0) * 0.6
        h_new = h_deg_new / 360.0
        s_new = min(1.0, max(0.0, s * (0.82 / 0.91)))
        l_new = min(1.0, max(0.0, l * (0.31 / 0.35)))
        r_new, g_new, b_new = colorsys.hls_to_rgb(h_new, l_new, s_new)
        return '#{:02x}{:02x}{:02x}'.format(int(r_new * 255 + 0.5), int(g_new * 255 + 0.5), int(b_new * 255 + 0.5))
    return '#' + hex_str

print("Color mappings:")
for c in colors_in_svg:
    mapped = shift_color(c)
    print(f"  {c} -> {mapped}")
