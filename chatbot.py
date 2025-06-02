def chatbot():
    print("🤖 Hello! I'm SimpleBot. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ['hi', 'hello']:
            print("SimpleBot: Hello there! 👋")
        elif 'name' in user_input:
            print("SimpleBot: I'm SimpleBot, your friendly chatbot.")
        elif 'how are you' in user_input:
            print("SimpleBot: I'm just a bunch of code, but thanks for asking! 😊")
        elif 'python' in user_input:
            print("SimpleBot: Python is an awesome programming language for beginners.")
        elif user_input in ['bye', 'exit', 'quit']:
            print("SimpleBot: Goodbye! Have a great day! 👋")
            break
        else:
            print("SimpleBot: Sorry, I don't understand that yet. 🤔")

if __name__ == "__main__":
    chatbot()
