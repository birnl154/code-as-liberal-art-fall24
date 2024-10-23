import markovify

text = open("unit-2/crops.txt").read()

generator = markovify.Text(text)

paragraph = "hello"

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")