import requests
from bs4 import BeautifulSoup
import random

# Make a request to the Cosmopolitan website
cosmo_response = requests.get("https://www.cosmopolitan.com")

# Get the HTML content using BeautifulSoup
cosmo_html = BeautifulSoup(cosmo_response.text, "html.parser")

# List of random clauses to put before to each item
clauses = [
    "This magazine talks about",
    "Women in our society should be interested in",
    "Woman need to care about",
    "This is important for women to know:",
    "Your next priority is learning about",
    "Women today are gossiping about",
]

def get_text_elements_with_clauses(cosmodata):
    # Select all <li> and <span> elements
    elements = cosmodata.select("span")
    
    # Extract, clean the text from each selected element, and add a random clause and period
    texts = [
        f"{random.choice(clauses)} {element.text.strip()}."
        for element in elements
        if element.text.strip()  # Only include if the text is not empty after stripping whitespace
    ]
    
    return texts

# Call the function to get the list of items with random clauses
texts_with_clauses = get_text_elements_with_clauses(cosmo_html)

# Join the text items into a single string
freeText = " ".join(texts_with_clauses)

# Write the result to a file if the list was properly populated
if freeText:
    with open('cosmo.txt', 'w') as cosmodata:
        cosmodata.write(freeText)

# Print confirmation
print("Text data successfully written to cosmo.txt")
