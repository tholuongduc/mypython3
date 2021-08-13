#Draw a star using Turtle
import turtle

star = turtle.Turtle()
star.pensize(5)
star.pencolor("blue")
for i in range(5):
    star.forward(100)
    star.right(144)
turtle.done()