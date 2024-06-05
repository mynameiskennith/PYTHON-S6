from tkinter import *
parent = Tk()

redbutton = Button(parent, text='Red',fg='red')
redbutton.pack(side=LEFT)

greenbutton = Button(parent, text='GREEN',fg='green')
greenbutton.pack(side=RIGHT)

bluebutton = Button(parent, text='BLUE', fg='blue')
bluebutton.pack(side=TOP)

blackbutton = Button(parent, text='BLACK',fg = 'black',command='p')
blackbutton.pack(side=BOTTOM)
parent.mainloop()

def p():
    print('Hi')