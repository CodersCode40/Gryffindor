# importing modules from the same directories:
import my_modules

course = ["math", "English", "physics", "computer"]

# find the index function: the "variable and the target"
index = my_modules.find_index(course, "English")
print(index)

# we can equally use a smaller name to replace my_modules
import my_modules as ko

# checking the sys
import sys

# printing out the index of a model:
models = ["toyota", "benz", "opel"]
key = ko.find_index(models, "opel")
print(key)

print(sys)

# importing a file from name; my_modules into this directories
import my_modules

print(my_modules.add(4, 2))
print(my_modules.subtruct(7, 4))
print(my_modules.square(3))