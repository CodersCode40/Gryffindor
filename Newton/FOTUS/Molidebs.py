'''String concatenating (aka how to put strings together)
Suppose we want to create a string that says "subscribe to____'''
youtuber = "LocalTECHGH" #Some string variable

# a few ways to do this
print("subcribe to " + youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ").strip().lower()
famous_person = input("famous person: ").title()

malib = f"Computer programming is so {adj}! It makes me so excited all the time because\
    I love to {verb1}. stay hydrated and {verb2} like you are {famous_person}!"

print(malib)