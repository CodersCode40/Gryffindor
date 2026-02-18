'''

Calculator building using functions
TODO
    - use functional Programming
    -- create functions for each operation
    --- use single variable to ask user opeation choice
    ---- use match-case to control the program flow
    ----- check for zerodivision error 
    ------ restrict user to enter only numbers => use 'While' and try-except
    ------- keep code clean (pls)

'''

def main():
     output = user_choice()
     print(output)


def user_choice():

    message = input (f"\n{"*"*10} simple Calculator {"*"*10} \n   SELECT OPERATION TO CONTINUE\n\n[1: ADDITION]\n[2: SUBSTRACTION]\n[3: MULTIPLICATION]\n[4: DIVISION]\npress 'n' to exit:  ").strip()
    match message:
        case "n" | "N":
            return "program exited ..."
        case _:
            num1, num2 = get_input()
            match message:
                case "1":
                    return addition(num1,num2)
                case "2":
                    return substraction(num1, num2)
                case "3":
                    return multiplication(num1, num2)
                case "4":
                    return division(num1,num2)
                case _:
                    return "invalid user choice [1 - 4] or 'n' to exit"


def get_input():
    
    while True:
        try:
            num1 = float(input("enter first number: \n"))
    
            num2 = float(input("enter second number: \n"))
            
            break
        except (ValueError, TypeError):
            print("enter valid input")
            continue
    return num1, num2



def addition(num1,num2):
    total = num1 + num2
    return f"Total: {int(total)}"



def substraction(num1, num2):
    total = num1 - num2
    return f"Total: {int(total)}"



def multiplication(num1, num2):
    total = num1 / num2
    return f"Total: {int(total)}"



def division(num1, num2):
    if num2 != 0:
        total = num1 / num2
        return f"Total: {total}"
    else:
        return "Can't divide by zero(0)"
    

if __name__ == "__main__":
    main()
