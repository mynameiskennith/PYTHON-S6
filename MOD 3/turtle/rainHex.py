import turtle

h = turtle.Turtle()
clr=['blue','green','yellow','orange','purple','black','magenta']
for i in range(150):
    h.color(clr[i%6])
    h.forward(i+1)
    h.left(59)
