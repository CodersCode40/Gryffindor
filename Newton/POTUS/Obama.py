'''Building a calculator'''
'''Creating a Function for Add, Subtract, Multibly, Divide'''
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        break
    except ValueError:
         print("Invalid input. Please enter numbers.")        
         continue
n = input("Enter Operation(+,-,*,/): ")


match n:
    case "+":
       print(add(x,y))
    case "-":
       print(subtract(x,y))
    case "/":
        print(divide(x,y))
    case "x":
        print(multiply(x,y))      