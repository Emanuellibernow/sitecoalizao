import os
from PIL import Image

def get_bbox(img_path):
    img = Image.open(img_path).convert('RGBA')
    # find bounding box of non-transparent and non-white pixels
    # (since background is white)
    width, height = img.size
    left, top, right, bottom = width, height, 0, 0
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if a > 10 and not (r > 245 and g > 245 and b > 245):
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
    return (left, top, right, bottom), (right - left), (bottom - top)

old_files = [
    ('logo_coalizao/02.png', 'Old 02'),
    ('logo_coalizao/Coalizão_logo_horizontal.png', 'Old Horizontal')
]

new_files = [
    (r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890148.png', 'New Attachment 0'),
    (r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890173.png', 'New Attachment 1'),
    (r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890189.png', 'New Attachment 2')
]

print("Bounding boxes and dimensions:")
for path, label in old_files + new_files:
    if os.path.exists(path):
        bbox, w, h = get_bbox(path)
        print(f"  {label} ({path}): size={Image.open(path).size}, bbox={bbox}, content_dim={w}x{h}, aspect={w/h:.3f}")
    else:
        print(f"  {label} ({path}) does not exist")
