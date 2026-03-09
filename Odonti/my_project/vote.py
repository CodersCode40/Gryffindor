# checking an eligibility to vote:

import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("input", "Enter Your name: ")
age = simpledialog.askinteger("input", "Enter your age: ")



def check_elegibility():
   
        if age >= 18:
            messagebox.showinfo("You are elegible")
        elif age < 18:
            messagebox.showinfo("Your are not elegible")
        else:
            messagebox.showinfo("You are dead")
    
check_elegibility()

root.destroy()