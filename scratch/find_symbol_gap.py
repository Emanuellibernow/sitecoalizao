import os
from PIL import Image

def find_symbol_gap():
    path = r'C:\Users\USER\.gemini\antigravity\brain\3e8019e7-64e9-4fe5-ad90-7b548641098d\media__1781793890173.png'
    if not os.path.exists(path):
        print("Image doesn't exist")
        return
    img = Image.open(path).convert('RGBA')
    width, height = img.size
    
    # Calculate non-white pixels count per row
    row_counts = []
    for y in range(height):
        count = 0
        for x in range(width):
            r, g, b, a = img.getpixel((x, y))
            if a > 10 and not (r > 245 and g > 245 and b > 245):
                count += 1
        row_counts.append(count)
        
    print("Row counts (first 100 non-zero rows):")
    non_zero_indices = [i for i, c in enumerate(row_counts) if c > 0]
    if not non_zero_indices:
        print("No non-zero rows found")
        return
    
    start_y = non_zero_indices[0]
    end_y = non_zero_indices[-1]
    print(f"Content spans from y={start_y} to y={end_y}")
    
    # Let's print row counts around the middle to find the gap (count = 0 or very small)
    for y in range(start_y, end_y + 1):
        print(f"y={y}: count={row_counts[y]}")
        
find_symbol_gap()
