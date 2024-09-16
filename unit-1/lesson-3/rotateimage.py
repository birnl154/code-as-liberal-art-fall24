

import sys
from PIL import Image

if len(sys.argv) > 1:
    image_path = sys.argv[1]
    
    try:
        img = Image.open(image_path)
        print("image loaded")
        
        rotated_img = img.rotate(90, expand=True)
        
        
        rotated_img.save("rotated_image.jpg")
        print("Rotated image saved as 'rotated_image.jpg'")
    
    except FileNotFoundError:
        print(f"File '{image_path}' not found.")
else:
    print("Please provide the image file path as an argument.")

