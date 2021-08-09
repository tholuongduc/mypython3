#Draw your dream house using turtle
import turtle
turtle.bgcolor("light blue")
turtle.shape("turtle")
turtle.speed(10)
turtle.pensize(3)
#Draw the front side
turtle.penup()
turtle.goto(-200,-200)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range (4):
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()
#Draw the main door
turtle.penup()
turtle.goto(-50,-200)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
for i in range (2):
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(100)
turtle.end_fill()
#Draw the right side
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.left(30)
turtle.forward(150)
turtle.left(60)
turtle.forward(200)
print(turtle.pos())
turtle.left(120)
turtle.forward(150)
turtle.goto(0,-200)
turtle.end_fill()
#Draw the windows
turtle.penup()
turtle.goto(50,-100)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.right(120)
turtle.forward(40)
turtle.right(60)
turtle.forward(50)
turtle.right(120)
turtle.forward(40)
turtle.goto(50,-100)
turtle.end_fill()
#Draw the roof top 1
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(-100,100)
turtle.goto(-200,0)
turtle.end_fill()
#Draw the roof top 2
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.left(120)
turtle.forward(150)
turtle.goto(129.90,75)
turtle.goto(0,0)
turtle.end_fill()
#Draw the sun
turtle.penup()
turtle.goto(300,300)
turtle.setheading(0)
turtle.pendown()
for i in range (4):
    turtle.left(45)
    turtle.forward(80)
    turtle.goto(300,300)
    turtle.left(45)
    turtle.forward(100)
    turtle.goto(300,300)
turtle.penup()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(300,250)
turtle.pendown()
turtle.circle(50)
turtle.end_fill()
#Draw the tree
turtle.penup()
turtle.goto(400,-300)
turtle.pendown()
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(425,-200)
turtle.pendown()
turtle.fillcolor("green")
turtle.begin_fill()
for i in range (3):
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(90)
    turtle.penup()
    turtle.forward(86.6)
    turtle.pendown()
    turtle.setheading(0)
turtle.end_fill()
turtle.penup()
turtle.goto(-100,-300)
turtle.setheading(90)
turtle.done()

