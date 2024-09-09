import sys
from PIL import Image 

img = Image.open( sys.argv[1])

print("You typed this filename:" + sys.argv[1])
print("This is a " + img.format)
print(img.format_description)
print("Size:" + str(img.size))