import sys
from assignment3data import *
# the asterisk means import all just fyi for future me

#you can reference the containers that you made in the data doc 
word_list.sort()
print(word_list)



## can we find the 2 bugs to find in this code?

# # # imports
# import sys
# from PIL import Image


# # Argument parsing
# args = sys.argv[1:] # args starting at index = 1
# if len(args) < 2: # if there aren't enough args
#     print("Not enough arguments") # tell them
#     exit(1) # and error

# # PIL instance initialization
# primary_image = Image.open(args[0])
# secondary_image = Image.open(args[1])
# blended_image = Image.blend(primary_image, secondary_image, .5) # images don't match error. tried different formats, matching sizes, ez
# blended_image.image('blended.jpg')

#last line needs to be blended_image.save('blended.jpg')











# # Good Comments!!!

# ## 1)
# import sys
# ## hint
# #from unit1lesson2 import word_list
# word_list = sys.argv
# ## this is saying that the word list that will be alphabetized are the arguments
# word_list.pop(0)
# ## .pop() so only user inputs are used
# ## argument has to be 1 so it doesn't include assignment name
# sortedlist = sorted(word_list)
# ## using sort function to alphabetize the words given in command line, or to alphabetize the arguments that are from the word list
# print (sortedlist)


# # last_word = sys.argv [0]
# # ## so last_word is a variable and it's saying that the last_word is the first item in the list
# # if sys.argv [1] > sys.argv [0]:
# #     last_word = sys.argv [1]
# # for word in word_list:
# #      ## word as a variable for all words in the list, making a loop to continue comparing
# #      if word > last_word:
# #           ## computer knows the alphabet, so if the word in the list is greater than what's made the last_word, which is the first item in the list
# #           last_word = word
# #           # if condition satisfied and the word in the list will become the new last_word

# # for word in word_list:
# #     if sys.argv[0] < sys.argv[1]:

# #     print(word_list)










### is there a way to blend 3 images at once??

# import sys
# from PIL import Image

# if len(sys.argv) != 3:
#     exit("This command requires one argument: the name of 2 image files")

# img1 = Image.open( sys.argv[1] )
# img2 = Image.open( sys.argv[2] )

# blended_img = Image.blend(img1,img2,.7) #images have to be the same size otherise it errors

# blended_img.save("blended3.jpg")

# ## i tried being crazy and blending 3 images all together at once like:
# if len(sys.argv) != 4:
#     exit("This command requires three arguments: the name of 3 image files")

# # img1 = Image.open( sys.argv[1] )
# # img2 = Image.open( sys.argv[2] )
# # img3 = Image.open( sys.argv[3] )

# # blended_img = Image.blend(img1,img2,img3,.5) #images have to be the same size otherise it errors

# ### that did not work out lol, my research said it would have to be like first two and then bledn again to the third?? how accurate that is im not sure








#### part 1 of assignment example

# import sys
# word_list = sys.argv 
# #data = [ 'badah', 'wants', 'to', 'code', 'better' ]
# #index = int(sys.argv)
# #print( data[index] )

# #pop removes the element from the list at the specified index. i.e 0
# word_list.pop(0)


# word_list.sort()
# print(word_list)










### can we find the bug in this code?

# import sys
# from PIL import Image

# if len(sys.argv) != 3:
#     print("Error: Please provide two image filenames.")
#     sys.exit(1)

# blended_img = Image.blend(img1,img2,.5)

# img1 = Image.open(sys.argv[1])
# img2 = Image.open(sys.argv[2])