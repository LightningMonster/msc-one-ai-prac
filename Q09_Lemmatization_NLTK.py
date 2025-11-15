# Code by Lightning Monster❤️
"""
Q.9) Write a Python program to implement Lemmatization using NLTK.
[20 Marks]
"""

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK data files (only once)
nltk.download('punkt')
nltk.download('punkt_tab')   # <-- Add this line to fix LookupError
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create Lemmatizer object
lemmatizer = WordNetLemmatizer()

# Input text
text = "The leaves on the trees are falling and the children are playing happily in the gardens."

# Tokenize text into words
words = word_tokenize(text)

print("Original Words:")
print(words)

# Perform Lemmatization
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("\nLemmatized Words:")
print(lemmatized_words)
