# Code by Lightning Monster❤️
"""
Q.11) Write a Python program to remove stop words for a given passage from a text file using NLTK.
[20 Marks]

Description:
Stop words are commonly used words in a language (like 'the', 'is', 'in', 'and') 
that usually do not contribute much to the meaning of a sentence.
This program reads text from a file, removes stop words using NLTK, 
and displays the cleaned output.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources (only first time)
nltk.download('punkt')
nltk.download('punkt_tab')   # for newer NLTK versions
nltk.download('stopwords')

# Step 1: Read text from a file
filename = "Q11_test.txt"

with open(filename, "r") as file:
    text = file.read()

print("📘 Original Text:\n")
print(text)

# Step 2: Tokenize the text
words = word_tokenize(text)

# Step 3: Get English stop words
stop_words = set(stopwords.words('english'))

# Step 4: Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words and word.isalpha()]

# Step 5: Display cleaned text
print("\n🧹 Text after removing stop words:\n")
print(" ".join(filtered_words))
