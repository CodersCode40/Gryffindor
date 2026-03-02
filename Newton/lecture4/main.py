#import random
#print(random)


#import cowsay
#sys
from ast import arguments
import sys
#from sys import argv

#print(sys.argv)

# def my_sys_func():
#     '''accep some cli arguments
#     then use that to print somethig to the
#      console '''
#     arguments = sys.argv

# for arg in arguments[1:]:
#     if arg == "-m" or arg == "module":
#         print("modules")
#     elif arg == 'p' or arg == "path":
#         print("path")
#     else:
#         print("too few argument")    

# if __name__ == "__main__":
#     my_sys_func()

def my_sys_func():
    """Accept some CLI arguments
    then use that to print something to the console
    """
    
    arguments = sys.argv

    if len(arguments) < 2:
        print("Too few arguments")
        return

    for arg in arguments[1:]:
        if arg == "-m" or arg == "module":
            print("modules")
        elif arg == "-p" or arg == "path":
            print("path")
        else:
            print("Unknown argument")

if __name__ == "__main__":
    my_sys_func()

