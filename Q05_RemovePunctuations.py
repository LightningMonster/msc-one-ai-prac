"""
Q.5) Write a Python program to remove punctuations from the given string.
[20 Marks]
"""

# Define punctuation characters
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# Input string from user
input_str = input("Enter a string: ")

# Create an empty string to store result
no_punct = ""

# Remove punctuation characters
for char in input_str:
    if char not in punctuations:
        no_punct += char

# Display result
print("\nOriginal String: ", input_str)
print("String without punctuations: ", no_punct)
