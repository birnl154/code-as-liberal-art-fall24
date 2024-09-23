import sys
from PIL import Image

# if len(sys.argv) != 2:
#     exit("This command requires one argument: the name of an image file")
#     #if len(sys.argv) means give me all the arguments and if its not equal to 2, then i need at least 2

img = Image.open( sys.argv[1] )


rotated_img = img.rotate( int(sys.argv[2]) )

rotated_img.save("rotated-" + sys.argv[1])

#the save will save the new image under the same folder with the rotated tag 