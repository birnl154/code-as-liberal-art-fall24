#here i have to import the beautiful soup to parse a website, random which i will use to write my essay, and requests to call on the html of the website with BS4

import requests
from bs4 import BeautifulSoup
import random

# Get the data from Cosmopolitan website
cosmo_response = requests.get("https://www.cosmopolitan.com")

# Get the HTML content using BeautifulSoup
cosmo_html = BeautifulSoup(cosmo_response.text, "html.parser")

# List of random clauses to put before to each item that will be important when constructing the essay
clauses = [
    "This magazine talks about",
    "Women in our society should be interested in",
    "Women need to care about",
    "This is important for women to know:",
    "Your next priority is learning about",
    "Women today are gossiping about",
]

#this line below is where i outline phrases found on the website i want to exclude. while they have the span tag, they are not really the same content as the rest of the span elements that i am trying to target.
excluded_phrases = ["search", "sign in", "Join cosmo Unlocked", "By", "*"]

#Here i am getting the span elements because they are most relevant to my project idea compared to other HTML elements
#the random shuffle is making it so i get a new order and range of span elements to include in my short essay each time the code is run.
def get_text_elements_with_clauses(cosmodata):
    elements = cosmodata.select("span", "li", "p")
    random.shuffle(elements)
    
    # This will get rid of any empty span elements so my essay doesn't look weird. 
    #i am using the random element here because i dont want the essay to all be in the same order
    #the last line regards me targeting the "search" and "sign in" that appeared in my final essay that i did not want because it is not relevant to the content, it is about the function of the website
    # the .lower function makes the gatehred text from the website into lowercase so it is able to properly identify if it matches my excluded phrases
    texts = [
        f"{random.choice(clauses)} {element.text.strip()}."
        for element in elements
        if element.text.strip()  
        and all(phrase.lower() not in element.text.strip().lower() for phrase in excluded_phrases)
    ]
    
    return texts

# Call the function to get the list of items with random clauses
texts_with_clauses = get_text_elements_with_clauses(cosmo_html)

# Join the text items into a single string and then it will add a period to make it legible as an essay
essay = " ".join(texts_with_clauses)

# set parameters for the needed word count of our unit 2 essay
paragraph = ""
wordcount = 0
min = 250
max = 300

# Add sentences until the word count is between 250-300
for sentence in texts_with_clauses:
    sentence_word_count = len(sentence.split())
    
    # Check if adding sentence will exceed 300, if it does then stop
    if wordcount + sentence_word_count > max:
        break 
    
    # Add the sentence to the paragraph and update the word count
    paragraph += sentence + " "
    wordcount += sentence_word_count

# Write the result to a file if the list was properly populated
if wordcount >= min:
    with open('cosmo.txt', 'w') as cosmodata:
        cosmodata.write(paragraph.strip())  # Strip to remove any trailing spaces



# Print confirmation to ensure the job was completed
print("Essay successfully written in cosmo.txt")
