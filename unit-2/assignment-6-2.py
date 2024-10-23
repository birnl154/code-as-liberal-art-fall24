import requests
from bs4 import BeautifulSoup

website_response = requests.get("https://www.wikihow.com/Budget-Your-Money")
website_soup_html = BeautifulSoup(website_response.text, "html.parser")

def getSpecificElements(soupdata, element_name):  
  website_data = open('crops.txt', 'w')
  elements = soupdata.select(element_name)
  print(elements)  

  if elements:
    for t in elements:
       plaintext = t.text.strip()
       website_data.write(str(plaintext))
    website_data.close()

getSpecificElements(website_soup_html, ".step")

#the question i asked for this data set is: what article will enhance the effect of the data txt I gathered? i thought it would then be interesting to put the biotech crop data against budgeting because i think it brings up the idea that we spend so much money on produce now because of rising prices and they are very artifical. So we are paying extremely high prices for artifical products that are sold as natural.