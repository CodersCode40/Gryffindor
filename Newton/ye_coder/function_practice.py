# What is scope and how do they work in python
'''Scope determine the visibility and accessibility of variables within a program. In Python, there are four types of scope:
1. Local Scope: Variables defined inside a function are local to that function.
2. Enclosing Scope: Variables in the enclosing function's scope.
3. Global Scope: Variables defined at the top level of a module or declared with 'global'.
4. Built-in Scope: Reserved names in Python like 'print', 'len', etc.
   
'''

# Local scope example
def my_function():
    local_var = "I am a local variable"
    print(local_var)

my_function()

# Enclosing scope example
def outer_function():
    new = "I am an enclosing variable"
    
    def inner_function():
        print(new)
        
    inner_function()
        
outer_function()

# Global scope example
global_var = "I am a global variable"