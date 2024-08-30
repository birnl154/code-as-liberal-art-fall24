

# Print a blank line
print("\n")

# Ask the user for a filename
filename = input("Please enter the name of a file in this directory: ")

# Open that file
file = open(test2.py)

print("Name is: " + file.readline())
print("Title is: " + file.readline())
print("Phone number is: " + file.readline())
print("Address is: " + file.readline())

For some reason, i have gotten errors messages saying "FileNotFoundError: [Errno 2] No such file or directory: 'guessing_game.py'"  or "command not found"
i tried this one for a long time, but i don't think i understand python enough to figure out what is going wrong here :(