import os
from PIL import Image

def analyze_transparency(path, name):
    if not os.path.exists(path):
        print(f"{name} does not exist")
        return
    img = Image.open(path)
    mode = img.mode
    print(f"{name} ({path}): Mode={mode}")
    if mode in ('RGBA', 'LA') or (mode == 'P' and 'transparency' in img.info):
        # check if it actually has transparent pixels
        alpha = img.convert('RGBA').split()[3]
        min_alpha, max_alpha = alpha.getextrema()
        print(f"  Alpha range: {min_alpha} to {max_alpha}")
        if min_alpha < 255:
            print("  Has transparent pixels!")
        else:
            print("  No transparent pixels (fully opaque)")
    else:
        print("  Fully opaque (no alpha channel)")

analyze_transparency('logo_coalizao/02.png', 'Old 02')
analyze_transparency('logo_coalizao/Coalizão_logo_horizontal.png', 'Old Horizontal')
analyze_transparency(r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890148.png', 'New Attachment 0')
analyze_transparency(r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890173.png', 'New Attachment 1')
analyze_transparency(r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890189.png', 'New Attachment 2')
