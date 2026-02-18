#Finishing Conditions , if statement , control flows modulo , match
"""
    using the operators in python to come up with condition 
    a == b 
    a >  b
    5 >= 5
    5 != 5

"""

"""
if conditions:

    if condition :
        pass
        
    if a == b :
        pass
    if a :
        pass
         4
    
# """
# def check_num():
#     value = input("what number do you choose ? : ")
#     if value < "6":
#         print('less than 6')
#     elif value > "20":
#         print("greater than 20")
#     elif value > "50":
#         print("greater than 50")
#     else:
#         print("the number is exactly the same .")

# check_num()


def check_day():
    day = input('enter a day of the week : ')

    match day:
        case "monday":
            print("Monday")
        case "tuesday":
            print("tuesday")
        case _:
            print("You need prayers")

check_day()

pr