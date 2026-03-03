# import random

# coin = random.choice(["Heads", "Tails", "legs"])
# print(coin)


# import math
# print(math.sqrt(16))
# print(math.sqrt(12,))
# print(math.sqrt(25))


# import random

# number = random.randint(1, 10)
# print(number)

# import random

# cards = ["queen", "king", "jack"]
# random.shuffle(cards)
# for card in cards:
#     print(card)


# # import random
# # names = ["ben", "gifty", "son", "joy"]
# # random.shuffle((names))
# # for name in names:
# #     print(name)


# import random
# names = random.choice(["ben", "gifty", "son", "joy"])
# print(names)

# # using a statistics library:
# import statistics
# print(statistics.mean([100, 90]))

# # # using the sys and argv:
# # import sys

# # try:
# #     print("hello, my name is", sys.argv[1])
# # except IndexError:
# #     print("Too few argument")



# import sys

# if len(sys.argv) <2:
#     print("Too few argument")
# elif len(sys.argv) >2:
#     print("Too many argument")
# else:
#     print("Hello my name is", sys.argv[1])


# import sys
# if len(sys.argv) < 4:
#     print("I love")
# elif len(sys.argv) > 4:
#     print("You are my enemy")
# else:
#     print("Come home", sys.argv[6])





# import nltk
# nltk.download('punkt')

# from nltk.tokenize import word_tokenize

# text = "Natural Language Processing is very interesting."

# # Break sentence into words
# words = word_tokenize(text)

# print("Tokenized words:")
# print(words)



# import sys
# from sys import math
# # # or 
# # from sys import argv, exit

# # argv = ["james", "ben"]

# # print(argv)


# print(sys.argv)




# import sys

# def my_sys():
#     argument = [sys.argv]
#     for arg in argument:
#         if arg == "-m" or arg == "module":
#             print("module")
#         elif arg == "-p" or arg == "path":
#             print("path")
#         else:
#             print("too few argument")
# my_sys()



# import sys
# if len(sys.argv) <1:
#     sys.exit("too many argument")

# for arg in sys.argv:
#     print("Hello, my name is", arg)


# import random
# import time
# import sys

# def get_computer_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)

# def determine_winner(user, computer):
#     if user == computer:
#         return "It's a tie!"
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         return "You win!"
#     else:
#         return "Computer wins!"

# def main():
#     print("🎮 Welcome to Rock, Paper, Scissors!")
    
#     while True:
#         user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
#         if user_choice == "quit":
#             print("Thanks for playing!")
#             sys.exit()

#         if user_choice not in ["rock", "paper", "scissors"]:
#             print("Invalid choice. Try again.")
#             continue

#         print("Computer is choosing...")
#         time.sleep(1)

#         computer_choice = get_computer_choice()

#         print(f"You chose: {user_choice}")
#         print(f"Computer chose: {computer_choice}")

#         result = determine_winner(user_choice, computer_choice)
#         print(result)

# if __name__ == "__main__":
#     main()




#     import random
# import time
# import sys
# import os

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def get_computer_choice():
#     return random.choice(["rock", "paper", "scissors"])

# def determine_winner(user, computer):
#     if user == computer:
#         return "tie"
#     elif (user == "rock" and computer == "scissors") or \
#          (user == "paper" and computer == "rock") or \
#          (user == "scissors" and computer == "paper"):
#         return "user"
#     else:
#         return "computer"

# def main():
#     user_score = 0
#     computer_score = 0
#     rounds = 0

#     print("🎮 Welcome to Rock, Paper, Scissors!")
    
#     while True:   # LOOP
#         print("\n1. Play")
#         print("2. Quit")
#         choice = input("Choose an option: ")

#         if choice == "2":   # CONDITION
#             print("Thanks for playing!")
#             sys.exit()

#         elif choice == "1":
#             clear_screen()
#             user = input("Enter rock, paper, or scissors: ").lower()

#             if user not in ["rock", "paper", "scissors"]:  # CONDITION
#                 print("Invalid choice!")
#                 continue

#             print("Rock...")
#             time.sleep(0.5)
#             print("Paper...")
#             time.sleep(0.5)
#             print("Scissors...")
#             time.sleep(0.5)
#             print("Go!\n")

#             computer = get_computer_choice()

#             print(f"You chose: {user}")
#             print(f"Computer chose: {computer}")

#             result = determine_winner(user, computer)

#             if result == "user":
#                 print("✅ You win this round!")
#                 user_score += 1
#             elif result == "computer":
#                 print("❌ Computer wins this round!")
#                 computer_score += 1
#             else:
#                 print("🤝 It's a tie!")

#             rounds += 1

#             print(f"\nScore after {rounds} rounds:")
#             print(f"You: {user_score}")
#             print(f"Computer: {computer_score}")

#         else:
#             print("Invalid menu option!")

# if __name__ == "__main__":
#     main()




import time

def traffic_light():
    while True:
        print("Red-stop")
        time.sleep(5)
        print("Yellow-Get Ready")
        time.sleep(2)
        print("Green-Go")