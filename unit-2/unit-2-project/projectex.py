import requests
from bs4 import BeautifulSoup
import random
import markovify

# Get the data from Cosmopolitan website
cosmo_response = requests.get("https://www.cosmopolitan.com")

# Check if the request was successful
if cosmo_response.status_code != 200:
    print("Failed to fetch the website data.")
else:
    print("Successfully fetched the website data.")

# Get the HTML content using BeautifulSoup
cosmo_html = BeautifulSoup(cosmo_response.text, "html.parser")

# Phrases to exclude from final text
excluded_phrases = ["search", "sign in", "Join cosmo Unlocked", "By", "*"]

# List of random clauses to prepend
clauses = [
    "This magazine talks about",
    "Women in our society should be interested in",
    "Women need to care about",
    "This is important for women to know:",
    "Your next priority is learning about",
    "Women today are gossiping about",
]

# Function to extract and clean the text from <li>, <span>, <p>, and <h1> elements
def get_random_text_elements_with_clauses(cosmodata):
    elements = cosmodata.select("li, span, p, h1")  # Corrected line
    random.shuffle(elements)  # Randomize order of elements

    texts = [
        f"{random.choice(clauses)} {element.text.strip()}."
        for element in elements
        if element.text.strip()
        and all(phrase.lower() not in element.text.strip().lower() for phrase in excluded_phrases)
    ]
    
    print(f"Extracted {len(texts)} elements after filtering.")
    return texts

texts_with_clauses = get_random_text_elements_with_clauses(cosmo_html)

# Check if we have enough data for markovify
if not texts_with_clauses:
    print("No valid text elements found. Exiting.")
else:
    # Combine the gathered sentences
    text_data = " ".join(texts_with_clauses)
    print("Text data prepared for Markov model.")

    # Train Markov model
    text_model = markovify.Text(text_data)

    paragraph = ""
    word_count = 0
    min_words = 250
    max_words = 300

    # Generate text using Markov model
    while word_count < max_words:
        sentence = text_model.make_sentence()
        
        if sentence:
            sentence_word_count = len(sentence.split())
            if word_count + sentence_word_count > max_words:
                break
            paragraph += sentence + " "
            word_count += sentence_word_count

    # Check if we met the minimum word count
    if word_count >= min_words:
        with open('new.txt', 'w') as cosmodata:
            cosmodata.write(paragraph.strip())
        print(f"Generated essay with {word_count} words written to new.txt.")
    else:
        print(f"Generated text only contains {word_count} words, less than the minimum required.")
