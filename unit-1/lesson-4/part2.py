import sys
from PIL import Image 

#i changed original code to 5 to accomodate four files instead
if len(sys.argv) != 5:
    exit("This program requires two arguments: the name of two image files to combine.")


# open all images
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )

# resize all images so they are no bigger than 400x400
# but preserve the original aspect ratio
img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )
img3.thumbnail( (400,400) )
img4.thumbnail( (400,400) )

# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
new_image = Image.new( "RGBA", (600,600), "black" )

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (100,200) )

# the alpha trait puts a transparency on the image
img2.putalpha(100)
img3.putalpha(80)
img4.putalpha(120)

# paste in all images
new_image.alpha_composite(img2, (0,50) )
new_image.alpha_composite(img3, (150,280) )
new_image.alpha_composite(img4, (40,300) )

# save the resulting image
# Note that we must convert it to RGB with no alpha to save it as a JPEG
new_image.save("combined3.png")

# Alternatively, we could have avoided converting by saving it to a
# PNG like this (since PNGs allow alpha):
# new_image.save("new.png")


#i decided to use the code from class to help me out on this assignment because I originally had a lot of trouble with the image changing due to thinking there was a path error, so I haven't had a lot of practice. 