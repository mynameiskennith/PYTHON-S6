from tkinter import *
from tkinter import messagebox

parent = Tk()
parent.geometry('300x200')

messagebox.showinfo('nfo','info')
messagebox.showwarning('warn','This is a warning')
messagebox.showerror('eror 404','This is an Error')
messagebox.askquestion('Question','Sugam Ano?')
messagebox.askyesno('QUestion','Are you YOU?')
messagebox.askokcancel('Q','Njan enna povva..')
messagebox.askretrycancel('Q','sherikkum pote?')

parent.mainloop()