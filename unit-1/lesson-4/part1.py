import sys
from PIL import Image

img = Image.open( sys.argv[1] )
colorswitch = img.convert(mode="HSV")
colorswitch = colorswitch.getdata()

new_img_data = []

# Modify pixel values based on brightness
for p in colorswitch:
    # Check the V (brightness) value
    if p[2] < 30:
        # Set Hue, Saturation, and Value to arbitrary valid HSV values
        new_img_data.append((0, 255, 255))  # Setting to red 
    else:
        # Keep the original HSV value
        new_img_data.append(p)

# Create a new image with the modified data
new_colorswitch = Image.new("HSV", colorswitch.size)
new_colorswitch.putdata(new_img_data)

# Convert the modified HSV image back to RGB
img_rgb = new_colorswitch.convert("RGB")

# Save the modified image
img_rgb.save("colorswitch.jpg")

#new image is saved under "colorswitch"
