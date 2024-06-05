# from tkinter import *
# from datetime import date

# parent = Tk()

# def calculateAge():
#     birth_year = int(e1.get())
#     current_year = date.today().year
#     agee = current_year - birth_year
#     age.config(text=f"Your age is: {agee}")

# year = Label(parent,text='Enter Year')
# year.grid(row=0,column=0)

# e1 = Entry(parent)
# e1.grid(row=0,column=1)

# submit = Button(parent,text='Submit',command=calculateAge)
# submit.grid(row=1,column=0)

# age = Label(parent,text='')
# age.grid(row=2,column=0)

# parent.mainloop()



# import tkinter as tk
# from datetime import date

# def calculate_age():
#     try:
#         birth_year = int(birth_year_entry.get())
#         current_year = date.today().year
#         age = current_year - birth_year
#         age_label.config(text=f"Your age is: {age}")
#     except ValueError:
#         age_label.config(text="Invalid input! Please enter a valid year.")

# root = tk.Tk()
# root.title("Age Calculator")

# birth_year_label = tk.Label(root, text="Enter your birth year:")
# birth_year_label.pack()

# birth_year_entry = tk.Entry(root)
# birth_year_entry.pack()

# calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
# calculate_button.pack()

# age_label = tk.Label(root, text="")
# age_label.pack()

# root.mainloop()

from tkinter import *
from datetime import date

parent = Tk()

def calculate():
    dob = int(e1.get())
    current_year = date.today().year
    agee = current_year-dob
    age.config(text=f'Your age is {agee}')

Year = Label(parent,text='Enter your year :')
Year.pack()

e1 = Entry(parent)
e1.pack()

submit = Button(parent,text='Submit',command=calculate)
submit.pack()

age = Label(parent,text='')
age.pack()

parent.mainloop()