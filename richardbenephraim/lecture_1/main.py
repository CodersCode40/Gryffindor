'''
TODO
**condition**
 

'''


def main():
    #output = get_user_input()
    #print(output)
    day = user_match_case()
    print(day)



def get_user_input():
    
    user = input ("what is the day: \n").strip().lower()

    if user == "monday":
        print("Its  Monday")
    elif user == "tuesday":
        print("Today is Tuesday")
    elif user == "wednesday":
        print("today is Wednesday")
    elif user == "thursday":
        print("Today is Thursday")
    elif user == "friday":
        print("Today is Friday")
    elif user == "saturday":
        print("Today is Saturday")
    else:
        print("Today is Sunday")



# match case statemant

def user_match_case():
    user = input("enter the day of the week: \n[1 to 7]")
    match user:
        case "1":
            return "its MONDAY"
        case "2":
            return "its TUESDAY"
        case "3":
            return "its WEDNESDAY"
        case "4":
            return "its THURSDAY"
        case "5":
            return "its FRIDAY"
        case "6":
            return "its Saturday"
        case "7":
            return "its SUNDAY"
        case _:
            return "invalid user choice"



if __name__ == "__main__":
    main()
    








