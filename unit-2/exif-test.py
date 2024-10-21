#this imports from the pillow library and the exif editing library
from PIL import Image 
import piexif 
import os
print(os.getcwd())

#this defines what myimage is by connecting it to the image i want to extract data from
img = Image.open('unit-2/bookspread.jpg')

# #extact the exif data
# exifdata = piexif.load(Image.info['exif'])

# #here is me changing the ISO data
# exifdata['Exif'][piexif.ExifIFD.ISOSpeedRatings] = 200
# #insert the modified infor back into the image
# exif_bytes = piexif.dump(exifdata)

if 'exif' in img.info:
    exif_dict = piexif.load(img.info['exif'])
    img.save('unit-2/modified_image.jpg', 'jpeg', exif=piexif.dump(exif_dict))
    print("Image saved successfully!")
else:
    exif_dict = {"Exif": {}}
    print("No EXIF data found, creating a new EXIF dictionary.")



