import time
import random


def botSays(text):
    print("Bot:", end=" ", flush=True)
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(0.02)
    print()


def chatbot():
    responses = {
        "hi": "Hello! How can I assist you?",
        "how are you": "I am doing great, thanks for asking.",
        "your name": "I am Student Bot. Tell me about your academics.",
        "who made you": "I was proudly created by Samujjal Dutta during the CODSOFT AI Internship.",
        "suggest a study tip": "Break your study time into short intervals and try the Pomodoro method .",
        "give me a motivational quote": random.choice([
            "Believe in yourself. You're halfway there.",
            "Push yourself, because no one else is going to do it for you.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts."
        ]),
        "bye": "Goodbye!! Keep learning and exploring."
    }

    botSays("Hello! I am StudentBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            botSays(responses["bye"])
            break
        elif user_input in responses:
            botSays(responses[user_input])
        else:
            botSays("Sorry... I did not understand that. Try something else?")


chatbot()
