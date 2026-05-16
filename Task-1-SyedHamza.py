# Advanced Rule-Based AI Chatbot
# DecodeLabs Project 1

import random
from datetime import datetime

print("=" * 50)
print("🤖 Welcome to DecodeBot AI")
print("Type 'help' to see commands")
print("Type 'exit' to stop the chatbot")
print("=" * 50)

user_name = ""

while True:

    user = input("\nYou: ").lower()

    # EXIT
    if user in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a wonderful day 👋")
        break

    # GREETINGS
    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello there! 😊")

    # ASK NAME
    elif "my name is" in user:
        user_name = user.replace("my name is", "").strip()
        print(f"Bot: Nice to meet you, {user_name}! 🎉")

    elif "what is my name" in user:
        if user_name != "":
            print(f"Bot: Your name is {user_name} 😄")
        else:
            print("Bot: I don't know your name yet.")

    # BOT NAME
    elif "your name" in user:
        print("Bot: My name is DecodeBot 🤖")

    # HOW ARE YOU
    elif "how are you" in user:
        responses = [
            "I'm doing great!",
            "All systems are running perfectly 🚀",
            "I'm awesome today 😄"
        ]
        print("Bot:", random.choice(responses))

    # TIME
    elif "time" in user:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # DATE
    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # AI
    elif "ai" in user:
        print("Bot: AI means Artificial Intelligence.")

    # JOKES
    elif "joke" in user:
        jokes = [
            "Why did the computer go to school? To improve its byte! 😂",
            "Why was the computer cold? Because it left its Windows open! 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂"
        ]
        print("Bot:", random.choice(jokes))

    # MOTIVATION
    elif "motivate" in user:
        quotes = [
            "Success comes from consistency.",
            "Keep learning and keep growing 🚀",
            "Every expert was once a beginner."
        ]
        print("Bot:", random.choice(quotes))

    # SIMPLE CALCULATOR
    elif "calculate" in user:
        try:
            expression = input("Enter calculation (example 5 + 3): ")
            result = eval(expression)
            print("Bot: Result =", result)
        except:
            print("Bot: Invalid calculation.")

    # NUMBER GUESSING GAME
    elif "game" in user:
        secret = random.randint(1, 5)

        print("Bot: Guess a number between 1 and 5")

        guess = int(input("Your guess: "))

        if guess == secret:
            print("Bot: Correct! 🎉")
        else:
            print(f"Bot: Wrong! The number was {secret}")

    # HELP MENU
    elif "help" in user:
        print("""
📌 Available Commands:
- hi / hello
- my name is ...
- what is my name
- your name
- how are you
- time
- date
- ai
- joke
- motivate
- calculate
- game
- help
- exit
        """)

    # THANKS
    elif "thank" in user:
        print("Bot: You're welcome 😊")

    # UNKNOWN INPUT
    else:
        print("Bot: Sorry, I don't understand that yet.")