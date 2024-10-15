def chatbot():
    print("Hello! I'm a simple chatbot. Ask me anything or type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

def get_response(user_input):
    # Simple keyword-based responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you?": "I'm just a program, but thanks for asking!",
        "what is your name?": "I'm a simple chatbot without a name!",
        "what is the capital of france?": "The capital of France is Paris.",
        "what is 2 + 2?": "2 + 2 equals 4.",
    }

    return responses.get(user_input, "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()