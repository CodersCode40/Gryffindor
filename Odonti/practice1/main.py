# # changing an items
# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "blackcurrant"
# print(thislist)

# # changing a range of an items:
# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# this_list[1:3] = ["blackcurrant", "watermelon"]
# print(this_list)


# # insecting an item or items in a list:
# this_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# this_list.insert(2, "watermelon")
# print(this_list)




# # adding an item to a list using an append:
# this_list = ["apple", "banana", "cherry"]
# this_list.append("orange")
# print(this_list)



# # extending a list:
# this_list = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# this_list.extend(tropical)
# print(this_list)


# # removing a specific index:
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)




# # looping through a list:
# thislist = ["apple", "banana", "cherry"]
# for a in thislist:
#     print(a)

# this = ["apple"]
# for i in this:
#     print(i)


# thislist = ["apple", "banana", "cherry"]
# for x in range(len(thislist)):
#     print(thislist[x])


# thislist = ["apple", "banana", "cherry"]
# v = 0
# while v <  len(thislist):
#     print(thislist[v])
#     v += 1



# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]



# # looping to store new list:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)


# menu = ["banku", "fufu", "Ampesi", "jolof rice", "waakye"]
# my_menu = []
# for o in menu:
#     if "a" in o:
#         my_menu.append(o)

# print(my_menu)
# print("Thanks") 



# food = ["can", "fast", "good", "way", "far"]
# good = []
# for w in food:
#     if "f" in w:
#         good.append(w)

# print(good)
# print("my love")



# food = ["zoo", "can", "fast", "good", "way", "far"]
# food.sort()
# print(food)



# # sorting a list in descending order:
# thislist = [100, 50, 70, 23, 42]
# thislist.sort(reverse = True)
# print(thislist)



# # returning a number closer to 50
# def myfunc(n):
#     return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)




# def class_score(f):
#     return abs(f - 70)
# num = [20, 70, 60, 76, 34, 45, 88, 89]
# num.sort(key = class_score)
# print(num)




# num = [20, 70, 60, 76, 34, 45, 88, 89]
# mynum = num.copy()
# print(mynum)




# joining two list as concatenation:
list1 = ["a", "b", "c",]
list2 = [1, 2, 3]
list3 = list1 + list2

print(list3)
