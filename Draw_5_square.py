#Draw 5 square
import turtle

turtle.pensize(3)
turtle.right(90)
for j in range (5):
    for i in range(2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
    turtle.right(72)

turtle.done()

