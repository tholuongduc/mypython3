#DAY 4: Draw a rectangle
import turtle
rec = turtle.Turtle ()
m = 100
n = 150
for i in range (2):
    rec.forward(m)
    rec.left(90)
    rec.forward(n)
    rec.left(90)
turtle.done