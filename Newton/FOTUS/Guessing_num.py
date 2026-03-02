import random

'''def guess(x):
    random_number = random.randint(1, x)
    
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess >random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly')            
    attemp_made += 1
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''

#     while feedback != 'c'and low != high:
#         if low != high:
#            guess = random.randint(low, high)
#         else:
#             guess = low # could also be high b/c low = high  
#         feedback = input(f'Is {guess} too high (H), too low(L), or correct (C)?? ').lower
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1    

#     print(f'yey! The computer guessed your number, {guess}, correctly!')       

guess(10)     
'''


def main():
    number_guessing()


def number_guessing():
    attemp_made = 0
    total_attempt = 7

    magic = random.randint(1, 20)

    while attemp_made < total_attempt:
        while True:
            try:
                user = int(input("enter the number: \n"))
                break
            except (ValueError, TypeError):
                print("only numbers are allowed")

                continue
        attemp_made += 1
        if user == magic:
            print(f'Yay, congrats. You have guessed the number {magic} correctly \nyou guess it in {attemp_made} Attempt')
        elif user   < magic:
            print('Sorry, guess again. Too low.')
        elif user > magic:
            print('Sorry, guess again. Too High.')
    else:
        print(f"Sorry you have exhausted your attempts the guess number is {magic}")
    



if __name__ == "__main__":
    main()