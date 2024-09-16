import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This command requires one argument: the name of an image file")
    #if len(sys.argv) means give me all the arguments and if its not equal to 2, then i need at least 2

img = Image.open( sys.argv[1] )

img.save( sys.argv[1] + ".jpg" )
img.save( sys.argv[1] + ".gif" )
img.save( sys.argv[1] + ".tiff" )
img.save( sys.argv[1] + ".png" )








####################################################################################
####################################################################################
#PUT ONE red PIXEL

img = Image.open( sys.argv[1] )
one_pixel = img.getpixel( (0,0) )
#onne_pixel is the made-up name of the variable, getpixel is the made-up name of the function
#double parentheses is used for calling coordinate, first is x and second is y
#three (x,x,x) used for rgb reference 

print(one_pixel)

img.putpixel( (10,10), (255,0,0) )
img.save("new.jpg")








####################################################################################
####################################################################################
#PUT ONE red PIXEL BUT MAKE IT A PNG

img = Image.open( sys.argv[1] )
one_pixel = img.getpixel( (0,0) )

print(one_pixel)

img.putpixel( (10,10), (255,0,0) )
img.save("new.jpg")
img.save("new.png")








####################################################################################
####################################################################################
# FILTER PIXELS AS A LIST

img = Image.open( sys.argv[1] )
img_hsv = img.convert(mode="HSV")
img_hsv_data = img_hsv.getdata()


#code below makes a new empty list
# for= starts running code on a certain section of data
#is p[2] means if saturation is less than 55 then push code otherwise, let the pixel stay
#kind of has the same effect as posterizing or color range in photoshop 
#the else caviat keeps that info in the image otherwise it would only include the pixels affected in the if statement
new_img_data = []
for p in img_hsv_data:
    print(p)
    if p[2] < 55:
        new_img_data.append( (255,255,255) )
    else:
        new_img_data.append(p)


img_hsv.putdata(new_img_data)
img_rgb = img_hsv.convert("RGB")
img_rgb.save("filtered.jpg")





#####################################################################################
#####################################################################################
# ALTERNATIVE CODE FOR PIXEL FILTER

# img = Image.open( sys.argv[1] )

# img_hsv = img.convert(mode="HSV")

# (width,height) = img_hsv.size

# for x in range(width):
#     for y in range(height):
#         pixel = img_hsv.getpixel((x,y))
#         if pixel[2] < 55:
#             img_hsv.putpixel( (x,y), (255,255,255) )
# img_rgb = img_hsv.convert(mode="RGB")
# img_rgb.save("filtered-range.jpg")








#####################################################################################
#####################################################################################
# # GENERATE IMAGE  ---- TO RUN THIS FROM MY TERMINAL I WROTE
## python3 classnotes.py generative-1.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# img.save(sys.argv[1])












#####################################################################################
#####################################################################################
# # GENERATE IMAGE --- - Gradient ----  TO RUN THIS FROM MY TERMINAL I WROTE
## python3 classnotes.py generative-2.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# data = []
# for i in range(100):
#     pixel = (i, 0, 0)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])








# #####################################################################################
# #####################################################################################
# # # GENERATE IMAGE EX 1 - 400x400 ---- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-3.jpg 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# data = []
# for i in range(160000):
#     pixel = (i, 0, 255-i)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

















#####################################################################################
#####################################################################################
# # EX 2+3 MODULO --- TO RUN THIS FROM MY TERMINAL I WROTE
# ## python3 classnotes.py generative-4.jpg 



# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         pixel = (x % 255, 0, y % 255)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])
