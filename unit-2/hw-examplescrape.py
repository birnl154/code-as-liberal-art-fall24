# import requests
# from bs4 import BeautifulSoup

# cosmo_response = requests.get("https://www.cosmopolitan.com")

# cosmo_html = BeautifulSoup(cosmo_response.text, "html.parser")

# cosmo_text = cosmo_html.get_text()

# lists = []

# def getlists(cosmodata):
#     lists = cosmo_text(".li")
#     print(lists)
   

# getlists(cosmo_html)

# freeText = " ".join(lists)

# cosmodata = open('cosmo.txt', 'w')
# cosmodata.write(getlists)
# cosmodata.close()


import requests
from bs4 import BeautifulSoup

# Make a request to the Cosmopolitan website
cosmo_response = requests.get("https://www.cosmopolitan.com")

# Parse the HTML content using BeautifulSoup
cosmo_html = BeautifulSoup(cosmo_response.text, "html.parser")

# List to store the text content of list items
list = []

# Define the function to extract list items
def getlists(cosmodata):
    # Select all <li> elements (list items)
    elements = cosmodata.select("li")  # Select all <li> elements
    list = [li.text.strip() for li in elements]  # Extract and clean text
    print(list)

# Call the function to get the list of items
list = getlists(cosmo_html)


# Join the list items into a single string
freeText = " ".join(list)

# Write the result to a file
with open('cosmo.txt', 'w') as cosmodata:
    cosmodata.write(freeText)

# Print confirmation
print("Text data successfully written to cosmo.txt")
