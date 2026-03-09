email =  input("Whats you email? : ")

info = email.split("@")

if "@" in email and "." in email:
    print("Valid")


else: 
    print("Invalid")

