'''
Functions are reusable blocks of code that perform a specific task. They allow you to break down your code into smaller, more manageable pieces, making it easier to read and maintain. In Python, you can define a function using the `def` keyword, followed by the function name and parentheses. You can also pass parameters to the function to make it more flexible.
'''

# Using the built in function, input() to get user input
name = input("What is your name? ")
print(f'Hello, {name}')

# Using the built in function, print() to display output
def claculate_sum(a, b):
    print( a + b)
    
# Calling the function with arguments    
my_sum = claculate_sum(5, 10)
print(my_sum)

# Using the reture keyword to return a value from a function
def claculate_sum(a, b):
    return a + b
    
# Calling the function with arguments    
my_sum = claculate_sum(5, 10)
print(my_sum)

# What is scope and how does it work in Python?
# Scope refers to the region of a program where a variable is defined and can be accessed.
# In Python, there are four types of scope: local, enclosing, global, and built-in.

# Local scope means that a variable declared inside a function or class can only be accessed within that function or class.
def my_function():
    x = 10  # x is a local variable
    print(x)
    
    my_function()
    
# Enclosing scope means    