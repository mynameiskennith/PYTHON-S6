from tkinter import *

parent = Tk()
parent.geometry('200x200')

checkvar1 = IntVar()
checkvar2 = IntVar()
checkvar3 = IntVar()

chkbtn1 = Checkbutton(parent,text = 'C',variable='checkvar1',onvalue=1,offvalue=0).pack()
chkbtn2 = Checkbutton(parent,text='Java',variable=checkvar2,onvalue=1,offvalue=2).pack()
chkbtn3 = Checkbutton(parent,text='C++',variable=checkvar3,onvalue=1,offvalue=0).pack()

parent.mainloop()