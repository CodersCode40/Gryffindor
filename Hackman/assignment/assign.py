"""
create a custom function that will check for parity.
to determine if a number is even or odd.
"""
def parity():
    number = 2
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

parity()        




# # assignment 2: The assignment 1: rewrite the  parity function , use try , except and try again to make sure the user enters a number.


def main():
    parity = parity_function("put in number: \n")
    print(parity)



def parity_function(ask):
    
    while True:
        try:
            number = int(input(ask))
            break
        except (TypeError, ValueError) as e:
            print(e, " __ Please enter a valid number.")
            continue
    if number % 2 == 0:
        return f"{number} is even number."
    else:
        return f"{number} is odd number."

    

if __name__ == "__main__":
    main()


parity 
"""
