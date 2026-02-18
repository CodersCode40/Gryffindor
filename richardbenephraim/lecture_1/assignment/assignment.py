
"""
write a parity function that will check if a number is even or old
"""

def main():
    # out  = even_checker()
    

    out2 = even_checker_adv()
    print(out2)



def even_checker():
    get_input = int (input("enter number: "))

    if get_input % 2 == 0:
        return "number is even"
    else:
        return 'even is old'
    
def even_checker_adv():
    while True:
        try:
            user_input = int(input("enter number: "))
            break
        except (TypeError, ValueError):
            print(" enter valid number ")
            continue
    if user_input % 2 == 0:
        return "number is Even"
    else:
        return "number is old"
    

if __name__ == "__main__":
    main()