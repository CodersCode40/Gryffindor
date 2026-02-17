"""
def main():
    infomatiom = input("What is your name? ")
    print(f"Hello, {infomatiom}!")
    print("Welcome to the mens pub.")

main()
"""
# Function that insists on YES or NO

"""
def get_yes_no():
    while True:
        answer = input("Enter YES or NO: ").upper()
        
        if answer == "YES" or answer == "NO":
            return answer
        else:
            print("Please type YES or NO.")


get_yes_no()

"""
"""
# Function that insists on a positive number

def get_positive_number():
    while True:
        try:
            number = float(input("Enter a positive number: "))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")



get_positive_number()
"""

# Function that insists input is in a list

# def get_choice():
#     options = ["rock", "paper", "scissors"]
    
#     while True:
#         choice = input("Choose rock, paper, or scissors: ").lower()
        
#         if choice in options:
#             return choice
#         else:
#             print("Invalid choice.")

# get_choice()   


# writing a function called analyze_number. 
def analyze_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            if number > 0:
                print("The number is positive.")
            elif number < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

analyze_number()

