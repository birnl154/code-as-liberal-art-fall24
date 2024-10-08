# Working with the code examples in the lesson 4 notes create your own image by building up patterns of pixels using the modulo operator and other techniques from those examples. Try 2-3 versions of this and make sure the output images are saved in your assignment-4 folder and labelled accordingly. 

# Now create your own image by collaging together at least 4 different images specified on the command line. Try to bring in some pattern and transparency techniques from lesson 4 notes. Try 2-3 versions of this and make sure the output images are saved in your assignment-4 folder and labelled accordingly. 

# * for this assignment you should have two files, for example part1.py and part2.py and at least 4 images (generated by your code files) all saved in your unit-1/lesson-4/assignment-4 folder plus the original images you used as data!



 				
# import sys
# from PIL import Image

# img = Image.open( sys.argv[1] )
# colorswitch = img.convert(mode="HSV")
# colorswitch = colorswitch.getdata()

# new_img_data = []

# # Modify pixel values based on brightness
# for p in colorswitch:
#     # Check the V (brightness) value
#     if p[2] < 30:
#         # Set Hue, Saturation, and Value to arbitrary valid HSV values
#         new_img_data.append((0, 255, 255))  # Setting to bright yellow for visibility
#     else:
#         # Keep the original HSV value
#         new_img_data.append(p)

# # Create a new image with the modified data
# new_colorswitch = Image.new("HSV", colorswitch.size)
# new_colorswitch.putdata(new_img_data)

# # Convert the modified HSV image back to RGB
# img_rgb = new_colorswitch.convert("RGB")

# # Save the modified image
# img_rgb.save("colorswitch.jpg")






import sys
from PIL import Image 

if len(sys.argv) != 5:
    exit("This program requires two arguments: the name of two image files to combine.")


# open both images
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )

# resize both images so they are no bigger than 400x400
# but preserve the original aspect ratio
img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )
img3.thumbnail( (400,400) )
img4.thumbnail( (400,400) )

# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
new_image = Image.new( "RGBA", (600,600), "white" )

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (0,0) )

# add some transparency (alpha) to the second image
img2.putalpha(128)
img3.putalpha(70)
img4.putalpha(170)

# paste in the second image, preserving its new transparency
new_image.alpha_composite(img2, (200,200) )
new_image.alpha_composite(img3, (100,200) )
new_image.alpha_composite(img4, (10,50) )

# save the resulting image
# Note that we must convert it to RGB with no alpha to save it as a JPEG
new_image.save("combined.png")

# Alternatively, we could have avoided converting by saving it to a
# PNG like this (since PNGs allow alpha):
# new_image.save("new.png")