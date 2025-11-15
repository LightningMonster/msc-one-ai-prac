# Code by Lightning Monster❤️
"""
Q.14) Write a Python program to implement a Simple Chatbot.
[20 Marks]

Description:
A simple rule-based chatbot that responds to basic user inputs.
This chatbot uses keyword matching for small talk, greetings, and FAQs.
"""

import random
import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    questions = ["how are you", "how are you doing"]
    date_queries = ["date", "day", "today"]
    time_queries = ["time", "current time"]
    goodbye = ["bye", "goodbye", "see you", "exit", "quit"]

    # Greeting
    if any(word in user_input for word in greetings):
        return random.choice(["Hello!", "Hi there!", "Hey! How can I help you today? 😊"])

    # How are you
    elif any(word in user_input for word in questions):
        return random.choice(["I'm doing great! Thanks for asking.", "All good! How about you?", "Feeling awesome today!"])

    # Date and time responses
    elif any(word in user_input for word in date_queries):
        return f"Today's date is {datetime.date.today()}."

    elif any(word in user_input for word in time_queries):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    # About chatbot
    elif "your name" in user_input:
        return "I’m Evalnex Bot — your AI assistant created by Lightning Monster ❤️."

    elif "creator" in user_input or "who made you" in user_input:
        return "I was created by Lightning Monster ⚡ as part of an AI project!"

    # Farewell
    elif any(word in user_input for word in goodbye):
        return random.choice(["Goodbye! Have a great day! 👋", "See you soon!", "Bye! Take care!"])

    # Default response
    else:
        return random.choice([
            "I'm not sure I understand that 🤔",
            "Can you please rephrase that?",
            "Interesting... tell me more!",
            "Hmm, I’ll have to think about that!"
        ])

# --- Main Program ---
print("🤖 Simple Chatbot (type 'bye' or 'exit' to end)")
print("------------------------------------------------")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Goodbye! Have a nice day! 👋")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
