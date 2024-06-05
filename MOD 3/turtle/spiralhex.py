import turtle

s = turtle.Turtle()
turtle.speed(2)

for i in range(10):
    s.circle(5*i)
    s.circle(-5*i)