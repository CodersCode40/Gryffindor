# """Creating a social media chatbot
# take users input and alow the bot to reply it
# automatically
# """

def chatbot():
    print("Welcome to ODONTI's Media Bot' 🧔‍♂️")

    print("Type 'quit' or 'q' to exit")

    while True:
        user_message = input("User : " ).lower().strip()

        if user_message in ["quit", "q"]:
            print("Bot: Goodbye")
            break

        elif user_message in ["hello", "hi"]:
            print("Bot: Hello!, how can I help you today? ")

        elif "price" in user_message:
            print("Bot: Our charges are very affordable")

        elif user_message == "location":
            print("Bot: We are located at Kokofu")

        elif "Time" in user_message:
            print("Bot: Out office starts at 8:00 am and close at 9:00 pm")

        elif user_message == "order":
            print("Bot: You can place an order through our website")

        else:
            print("Bot: We are sorry, we didn't understand what you mean")


chatbot()