# Write a parity function to determine if a number is even or odd. The function should return "Even" for even numbers and "Odd" for odd numbers.def parity(num):
def parity():
    num = int (input("enter number: "))
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
output = parity()
print(output)