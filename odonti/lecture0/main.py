# # first funtion program
# name = input("what is your name:")
# # print("Hello World")
# print("hello, name")

# # another way to concatenate:
# print("Hello", end = " ")
# print(name)


# # fstrings
# print(f"Hello, '{name}'")

# # strip function:
# print(f"{name.strip()}")



# # addin integers:
# a = 4
# b = 5
# z = a + b
# print(z)

# # ask user for the numbers:
# num1 = int(input("whats num1: "))
# num2 = int(input("whats num2:"))
# m = num1 + num2

# a = int(input("whats a:"))
# b = int(input("whats b:"))
# v = a + b
# print(m , v)



# # ask users for their name and remove whitespace from the str and capitalize the first letter of each word:
# name = input("whats your name?: ").strip(). title()
# print(f"Hello, {name}")


# first_name = input("What is your first name?: ")
# last_name = input("What is your last name?: ")
# name = first_name.strip().title() + " " + last_name.strip().title()
# print(f"Hello, {name}")

# # DEF FUNCTIONS:
# def hello():
#     print("Hello World")
# hello()

# def name():
#     print("Isaac")
# name()

# def father():
#     print("Afrifa")
# father()

# def add():
#     a = 4
#     b = 5
#     c = a + b
#     print(c)
# add()

# from email import message


# def name():
#     name = input("whats your name?: ")
#     print("Hello,", name.strip().upper())
# name()


# # greetings with users name:
# def greet(name):
#     message = f"Hello, {name.strip().title()}"
#     return message
# greetings = greet("isaac")
# print(greetings)
# print(greetings)
# print(greetings)


# def cat():
#     print("meow")
# cat()
# cat()
# cat()

#  without using a function, this is how our code would be like:
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# with the help of a function:
def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

# a function that returns value:
def get_greetings():
    return "Hello, World"
message = get_greetings()
print(message)


def my_name():
    return "isaac".title()
name = my_name()
print(name)

def greetings():
    greet = f"Hello My dear, {my_name()}"
    return greet
message = greetings()
print(message)



def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
    




