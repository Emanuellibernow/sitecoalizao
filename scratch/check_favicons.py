import os
from PIL import Image

favicons = [
    'favicon/android-chrome-192x192.png',
    'favicon/android-chrome-512x512.png',
    'favicon/apple-touch-icon.png',
    'favicon/favicon-16x16.png',
    'favicon/favicon-32x32.png',
    'favicon/favicon.ico',
    'favicon/favicon.png'
]

print("Favicon files:")
for f in favicons:
    path = os.path.join('c:\\Users\\USER\\Documents\\Coalizao\\sitecoalizao-main', f)
    if os.path.exists(path):
        try:
            img = Image.open(path)
            print(f"  {f}: format={img.format}, size={img.size}, mode={img.mode}")
        except Exception as e:
            print(f"  {f}: error opening: {e}")
    else:
        print(f"  {f}: does not exist")
