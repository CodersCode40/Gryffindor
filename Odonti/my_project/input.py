import tkinter as tk
from tkinter import simpledialog, messagebox
 
root = tk.Tk()
root.withdraw()
name = simpledialog.askstring("input", "Enter your name: ").upper().strip()

age = simpledialog.askinteger("input", "Enter your Age: ")

messagebox.showinfo(f"Hello, my name is: {name}, I am {age} years old")

root.destroy()


