# While loop
i = 3
while i >= 0:
    print("meow")
    i -= 5


# For loop
for _ in "cat":
    print("c")
    
for letter in "cat":
    print(letter)
# Using range in loop    
animal = "cat"
for letter in range(len(animal)):
    print(animal[letter])

# Enumerate use case
for index, letter in enumerate(animal):
    print(letter, index)
    

def print_width():
    sign = "#"
    i = 0
    for i in range(6):
        print("#" * 5) # or i
print_width()      

# What are Eception (What are error)
try:
    print(a)
except NameError:
    print("NameError")    
# Runtime Error
    
    
        
            
    