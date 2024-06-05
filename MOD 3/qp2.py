# from tkinter import *
# from PIL import Image,ImageTk

# parent = Tk()

# image = Image.open('image.png')

# photo = ImageTk.PhotoImage(image)

# image_l = Label(parent,image=photo)
# image_l.pack()

# parent.mainloop()

from tkinter import *
from PIL import Image,ImageTk
parent = Tk()

image = Image.open('image.png')
photo = ImageTk.PhotoImage(image)

im = Label(parent,image=photo)
im.pack()

parent.mainloop()