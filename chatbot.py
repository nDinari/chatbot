# chatbot.py

import json
import random

# Load intents from JSON file
with open('intents.json', 'r') as file:
    intents = json.load(file)

# Function to handle user input
def handle_input(user_input):
    # Check if input matches any intent

    # Convert user input to lowercase
    user_input_lower = user_input.lower()
    for intent in intents['intents']:
        # Convert intent patterns to lowercase for comparison
        for pattern in intent['patterns']:
            if user_input_lower in pattern.lower():
                return random.choice(intent['responses'])

    # If no matching intent found, handle unknown intent
    return handle_unknown_intent(user_input)

# Function to handle unknown intent
def handle_unknown_intent(user_input):
    # Add unknown intent to intents.json file
    new_intent = {
        "tag": "unknown",
        "patterns": [user_input],
        "responses": ["I'm sorry, I didn't understand that."]
    }
    intents['intents'].append(new_intent)

    # Save updated intents to JSON file
    with open('intents.json', 'w') as file:
        json.dump(intents, file, indent=4)

    return random.choice(new_intent['responses'])

# Main function to simulate chat interaction
def main():
    print("Welcome to the HR chatbot!")
    print("Type 'quit' to exit.")

    while True:
        user_input = input("You: ")
         # Check for exit signals
        exit_signals = ["quit", "exit", "bye", "goodbye"]
        exit_responses = ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Come back soon!", "Farewell! Have a wonderful day!", "Take care! See you soon!"]
        if any(signal in user_input.lower() for signal in exit_signals):
            print("Bot:", random.choice(exit_responses))
            break

        response = handle_input(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
