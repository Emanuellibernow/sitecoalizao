import os
from PIL import Image

def verify_all():
    print("Verifying assets...")
    
    # 1. Logo paths
    logos = [
        'logo_coalizao/02.png',
        'logo_coalizao/Coalizão_logo_horizontal.png'
    ]
    for logo in logos:
        path = os.path.join('c:\\Users\\USER\\Documents\\Coalizao\\sitecoalizao-main', logo)
        if os.path.exists(path):
            try:
                img = Image.open(path)
                print(f"  [OK] Logo {logo} is a valid {img.format} image of size {img.size}")
            except Exception as e:
                print(f"  [ERROR] Logo {logo} failed to open: {e}")
        else:
            print(f"  [ERROR] Logo {logo} does not exist!")
            
    # 2. Favicon paths
    favicons = [
        'favicon/android-chrome-192x192.png',
        'favicon/android-chrome-512x512.png',
        'favicon/apple-touch-icon.png',
        'favicon/favicon-16x16.png',
        'favicon/favicon-32x32.png',
        'favicon/favicon.ico',
        'favicon/favicon.png'
    ]
    for fav in favicons:
        path = os.path.join('c:\\Users\\USER\\Documents\\Coalizao\\sitecoalizao-main', fav)
        if os.path.exists(path):
            try:
                img = Image.open(path)
                print(f"  [OK] Favicon {fav} is a valid {img.format} image of size {img.size}")
            except Exception as e:
                print(f"  [ERROR] Favicon {fav} failed to open: {e}")
        else:
            print(f"  [ERROR] Favicon {fav} does not exist!")
            
    # 3. SVG illustration
    svg_path = 'images/hero-coalizao-fluid-detailed.svg'
    if os.path.exists(svg_path):
        print(f"  [OK] SVG file {svg_path} exists. Size={os.path.getsize(svg_path)} bytes")
    else:
        print(f"  [ERROR] SVG file {svg_path} does not exist!")
        
    print("Verification completed.")

if __name__ == '__main__':
    verify_all()
