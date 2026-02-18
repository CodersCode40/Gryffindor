
# Using the built in function def
def focus_on_yourself():
    sentance = ("Focus on yourself and your own growth.")
    print(sentance)

# Using the input function to get user input
name = input("Fuck bitches: ")


focus_on_yourself()

# What are conditions
'''Conditions are used to perform different actions based on different conditions. In Python, you can use the `if`, `elif`, and `else` statements to create conditional statements. The `if` statement is used to test a specific condition, while the `elif` statement is used to test additional conditions if the previous conditions were not true. The `else` statement is used to execute a block of code if all the previous conditions were false.'''
'''using the operators in python to come up with condition
a == b
a > b
5 >= 5
5 != 5
'''
'''
if conditions:
    if comdition:
        pass
        
    if a == b:
        pass
    
    if a:
        pass    
'''

def check_out():
    j = input("Name of squad list: ")
    i = 0
    if i != j:
        print("Yes, you are part of the squad")
    
print("No, You are not part of the squad")
check_out            
    
'''
Control flows:

def check_num():
    value = input("What number do you choose)
    if value < "6":
    print('less than 6')
    elif value > 20:
    print('greater than 29')
    else:
          
    '''    
def days_of_the_week():
    days = input("What day is today? ")  
    i = 0
    if i != days:
        print("Today`s Monday")
    elif i > days:
        print("Today`s Tuesday")
    elif i < days: 
        print("Today`s Wednesday")
    elif i > days:
        print("Today`s Thusday")
    elif i > days:
        print("Today`s Friday")
    elif i > days:
        print("Today`s Saturday")               
    else:
        print("Today`s Sunday")    
        
days_of_the_week()       

# Match naming
def check_out():
    days = input("Enter a day of the week: ")
    
    match days:
        case "monday":
            print("Monday")
        case "tuesday":
            print("Tuesday")
        case "wednesday":
            print("You need prayers")        
    
# To be continued in the next lecture       
    

