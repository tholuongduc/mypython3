#Draw 5 square
import turtle
import random

color = ['black', 'red', 'blue', 'green', 'pink', 'orange']

turtle.speed(10)
turtle.pensize(3)
turtle.right(90)
for j in range (5):
    choice_color = random.choice(color)
    turtle.fillcolor(choice_color)
    for i in range(2):
        turtle.begin_fill()
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.end_fill()
    turtle.right(72)

turtle.done()

