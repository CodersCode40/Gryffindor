# import tkinter to alow us to use pyinstaller
import tkinter as tk
from tkinter import simpledialog, messagebox


root = tk.Tk()
root.withdraw()

# ask for users input:

name = simpledialog.askstring("Input", "Enter your name: ")
age = simpledialog.askinteger("Input", "Enter your age")
school = simpledialog.askstring("Input", "Enter your school: ")
marks = simpledialog.askinteger("Input", "Enter your marks")

# use if statement to check for grading system:
def check_pass_mark():
    if marks >= 80:
        messagebox.showinfo("Grade A", "Excilient")
    elif marks >= 70:
        messagebox.showinfo("Grade B", "Very Good")
    elif marks >= 60:
        messagebox.showinfo("Grade C", "Good")
    elif marks >= 50:
        messagebox.showinfo("Grade D", "Sit-up")
    else:
        messagebox.showinfo("Grade F", "Faild")

check_pass_mark()

root.destroy()