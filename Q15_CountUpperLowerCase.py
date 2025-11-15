# Code by Lightning Monster❤️
"""
Q.15) Write a Python program to accept a string. 
Find and print the number of upper case alphabets and lower case alphabets.
[20 Marks]
"""

# Input string from user
text = input("Enter a string: ")

# Initialize counters
upper_count = 0
lower_count = 0

# Loop through each character in the string
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

# Display results
print("\nOriginal String:", text)
print("Number of Uppercase Letters:", upper_count)
print("Number of Lowercase Letters:", lower_count)


# Hello, Lightning! How are you doing today?