import os
#import os means helps to navigate filing system 

import random
#i will need to randomize in this code, so this allows me to be able to do that

from PIL import Image
#this allows me to access and edit my images

head = 'head'
torso = 'torso'
legs = 'legs'
#here I am telling the code where to find these folders and defining them

headimg = Image.open(os.path.join(head, random.choice(os.listdir(head))))
torsoimg = Image.open(os.path.join(torso, random.choice(os.listdir(torso))))
legsimg = Image.open(os.path.join(legs, random.choice(os.listdir(legs))))
#this explains that the code needs to randomly get an image from each of the defined folders

canvas_width = 500
canvas_height = 200 + 200 + 400
canvas = Image.new('RGB', (canvas_width, canvas_height))
#this sets the parameters for the blank canvas that the images will be placed on

canvas.paste(headimg, (0, 0))                # Paste first at the top
canvas.paste(torsoimg, (0, 200))               # Paste second in the middle
canvas.paste(legsimg, (0, 400))               # Paste third at the bottom
#this actually pastes the chosen random images at the three appropriate spots on the blank canvas

random_number = random.randint(100, 999)  # Generates a number between 100 and 999
#this bit of code utilizes the randomization that we learned about in this unit to help with some errors. When I first ran the code, it kept saving the images on top of each other because they were all using the same name. I decided that each new image will now be saved with a random 3 digit number to help differeniate the images and prevent them for being saved on top of one another.

output_folder = 'final_images/'
#this indicates where the final images should be saved

output_filename = f"final_image_{random_number}.jpg"
#this bit of code gives the new image a file name in addition to using the random number function

output_path = os.path.join(output_folder, output_filename)
#this line joins together the path directory and the image file name so the program knows exactly where to save the images.



# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


try:
    canvas.save(output_path, 'JPEG')
    print(f"Final image saved at {output_path}")
except Exception as e:
    print(f"Error saving image, output folder not found: {e}")
    #this code is to help with error handling and took some researching to figure out since we didn't cover this in class. it uses the try/except format to have the code attempt to run the first part of the argument, whcih in this case is finding the output folder. If it can't find it, then it will print the error code that the output file was not found. This helps the user because it will specify what exactly went wrong when the program was not run successfully.
