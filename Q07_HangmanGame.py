# Code by Lightning Monster❤️
"""
Q.7) Write a Python program to implement the Hangman game.

Description:
Hangman is a classic word-guessing game. The user has to guess the correct word
by entering alphabets of their choice. The program takes a single alphabet as input
and matches it with the letters of the original word.
"""

import random

# List of words for the game
words = ["python", "hangman", "computer", "science", "programming", "developer", "machine"]

# Select a random word from the list
word = random.choice(words)
guessed_letters = []
attempts = 6  # Total chances for the player

print("🎯 Welcome to the Hangman Game!")
print("You have", attempts, "lives to guess the word correctly.\n")

# Display underscores for each letter
while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())

    # Check if player has guessed all letters
    if all(letter in guessed_letters for letter in word):
        print("\n🏆 Congratulations! You guessed the word correctly:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet only.\n")
        continue

    # If letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("✅ Good guess!\n")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} lives left.\n")

# If player fails
if attempts == 0:
    print("💀 Game Over! The correct word was:", word)
