# chatbot.py

import json
import random
import re

class EnterpriseChatbot:
    def __init__(self, intents):
        self.intents = intents

    def get_response(self, user_input):
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                # Use regular expression to match patterns with user input
                # print("Matching pattern:", pattern)
                if re.match(pattern.replace('[', '\[').replace(']', '\]').replace('product_name', '(.*)').replace('order_number', '(.*)'), user_input):
                    responses = intent['responses']
                    return random.choice(responses)
        # Fallback response if no intent is matched
        # print("No matching intent found.")
        return random.choice(self.intents['intents'][-1]['responses'])


if __name__ == "__main__":
    # Load intents from JSON
    with open('intents.json', 'r') as file:
        intents = json.load(file)

    # Initialize the chatbot
    chatbot = EnterpriseChatbot(intents)

    # Chat loop
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.get_response(user_input)
        print("Chatbot:", response)
