import turtle

t = turtle.Turtle()
j=0
while j!=200:
    for i in range(5):
        t.circle(10*j,90)
        t.left(90)
        t.circle(10*j,90)
        t.left(18)
    j+=1

turtle.done()