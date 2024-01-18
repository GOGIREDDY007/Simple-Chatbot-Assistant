class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I help you today?"

    def farewell(self):
        return "Goodbye! Have a great day."

    def handle_question(self, question):
        if "how are you" in question.lower():
            return "I'm just a chatbot, but thanks for asking!"
        elif "your name" in question.lower():
            return "I'm a simple chatbot, you can call me ChatGPT."
        elif "weather" in question.lower():
            return "I'm sorry, I don't have access to real-time weather information."
        elif "your purpose" in question.lower():
            return "I'm here to assist you with basic questions and tasks."
        elif "bye" in question.lower() or "goodbye" in question.lower():
            return self.farewell()
        else:
            return "I'm not sure how to answer that. Can you please ask a different question?"

    def user_interaction(self):
        questions = [
            "What's your name?",
            "How are you today?",
            "Can you tell me the weather?",
        ]

        for i in range(3):
            user_response = input(self.handle_question(questions[i]) + "\nYour response: ")
            self.context[f"Q{i+1}"] = user_response

        print("\nThank you for chatting with me!")

    def start_chat(self):
        print(self.greet())
        self.user_interaction()


if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.start_chat()
