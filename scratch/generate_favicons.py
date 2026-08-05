import os
from PIL import Image

def generate_favicons():
    src_path = r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890173.png'
    if not os.path.exists(src_path):
        print(f"Source {src_path} not found")
        return
        
    img = Image.open(src_path).convert('RGBA')
    
    # Bounding box of the symbol (the infinity loop)
    # We found: left=52, top=301, right=627, bottom=521
    left, top, right, bottom = 52, 301, 627, 521
    symbol = img.crop((left, top, right, bottom))
    
    # Create a square canvas (w x w)
    w = right - left # 575
    square_canvas = Image.new('RGBA', (w, w), (255, 255, 255, 0))
    
    # Center the symbol vertically
    h = bottom - top # 220
    y_offset = (w - h) // 2
    square_canvas.paste(symbol, (0, y_offset), symbol)
    
    # Define outputs
    outputs = {
        'favicon/android-chrome-192x192.png': (192, 192),
        'favicon/android-chrome-512x512.png': (512, 512),
        'favicon/apple-touch-icon.png': (180, 180),
        'favicon/favicon-16x16.png': (16, 16),
        'favicon/favicon-32x32.png': (32, 32),
        'favicon/favicon.ico': (48, 48)
    }
    
    for dest, size in outputs.items():
        dest_path = os.path.join('c:\\Users\\USER\\Documents\\Coalizao\\sitecoalizao-main', dest)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        # Resampling filter: LANCZOS (Resampling.LANCZOS is Image.LANCZOS)
        resized = square_canvas.resize(size, Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
        
        if dest.endswith('.ico'):
            # ICO format can store multiple sizes, or single size
            resized.save(dest_path, format='ICO', sizes=[size])
        else:
            resized.save(dest_path, format='PNG')
        print(f"Generated {dest_path} with size {size}")
        
    # Also replace favicon.png (which was 1536x1024) with the new transparent horizontal logo
    horizontal_logo_src = r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890189.png'
    favicon_png_dest = r'c:\Users\USER\Documents\Coalizao\sitecoalizao-main\favicon\favicon.png'
    if os.path.exists(horizontal_logo_src):
        # copy directly
        import shutil
        shutil.copy(horizontal_logo_src, favicon_png_dest)
        print(f"Copied horizontal logo to {favicon_png_dest}")

if __name__ == '__main__':
    generate_favicons()
