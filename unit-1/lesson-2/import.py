from unit1lesson2 import *





# 1111111111111111111111111111111111111111111111111

# # ...... Lara

# smallestnumber = number_list[0]
# if number_list[1] < smallestnumber:
#     smallestnumber = number_list[1]
# for x in number_list:
#     if x < smallestnumber:
#         smallestnumber = x
# print(smallestnumber)
# # ..... E1 Answer is 175




#.......Paulina

# number_list.sort()
# print("The smallest number is:", number_list[0])



















# 22222222222222222222222222222222222222222222


# # ...... Beimnet
# number_list.sort()

# for x in number_list:
#     if x > 500:
#         print(x) # answer is 501
#         break



# # ...... Lara

# smallestnumberover500 = number_list[0]
# if number_list[1] < smallestnumberover500:
#     smallestnumberover500 = number_list[1]
# for x in number_list:
#     if 500 < x < smallestnumberover500:
#         smallestnumberover500 = x
# print(smallestnumberover500)



















# 33333333333333333333333333333333


# #...... Chris

# number_list.sort()
# even_numbers = []

# for num in number_list:
#     if num % 2 == 0:
#         even_numbers.append(num)
    
# even_numbers.sort()
# print(even_numbers[0])


# #smallest even number is 176










# ###### lets make our own "sort" function to get smallest even number

# #define a function
# def sortSmallToBig(wholeList):
#     # #use Lara's algorithm
#     smallest = wholeList[0]
#     if wholeList[1] < smallest:
#         smallest = wholeList[1]
#     for x in wholeList:
#         if x < smallest:
#             smallest = x  
#     return smallest



# #now use Chris' algorithm
# even_numbers = []

# for num in number_list:
#     if num % 2 == 0:
#         even_numbers.append(num)


# smallestEven = sortSmallToBig(even_numbers)

# print(smallestEven)






# # a small bug that you might run into!

# small_list = [ 3, 10, 4, 14, 22, 11 ]
# # write a variable for smallest even number called sen
# sen = 0
# #  first number is an odd number, and it is smaller than all the even numbers. In a case like this it initially sets sen to number_list[0], it will set it to 3, and when the code loops through the list, as it encounters small even numbers, those numbers will never be smaller than 3, so the code will never consider them to be smallest even number, and so when the loop finishes running, sen will still be 3, which is wrong because this is an odd number. we can avoid this issue by setting the smallest number to 0 instead of the first number in the list.

# for n in small_list:
#     if n % 2 == 0:
#         #will only run now with 10, 4, 14, 22
#         if n < sen or sen == 0:
#             # if 10 is smaller than 0 or SEN is set to 0 still
#             # make the SEN equal to 10
#             # if 4 is smaller than 10 or sen is set to 0 still
#             # make the SEN equal to 4
#             # if 14 is smaller than 4 or SEN is set to 0 still
#             # SEN doesn't get reset because this is false, same for 22
#             sen = n

# print("The smallest even number in this list is: " + str(sen) )










# ### 444444444444444444444444444444444444444

# ## find the alphabetically last word in the word list

# alphabetically_last_word = word_list[0]

# for word in word_list:
#     if word > alphabetically_last_word:
#         alphabetically_last_word = word

# print("The last word (alphabetically) is", alphabetically_last_word)









# ### 555555555555555555555555555

# ##find the longest word in the word list
# longest_word = word_list[0]

# for word in word_list:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("The longest word is", longest_word)