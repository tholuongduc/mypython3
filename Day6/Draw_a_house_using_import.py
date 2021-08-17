import turtle
import math
import Rectangle
import Triangle
import cloud
#Background color
turtle.bgcolor("yellow")

turtle.shape("turtle")
turtle.speed(15)
#Draw the front house
Rectangle.drawRectangle(turtle, 300, 150, "orange")
#Draw the main door
turtle.penup()
turtle.goto(120,0)
turtle.pendown()
Rectangle.drawRectangle(turtle, 60, 80, "brown")
#Draw the chimney
turtle.penup()
turtle.goto(150,150)
turtle.pendown()
Rectangle.drawRectangle(turtle, 20, 80, "red")
#Draw the roof top
turtle.penup()
turtle.goto(0,150)
turtle.pendown()
Triangle.drawTriangle(turtle, 200, "red")
#Draw the smoke
turtle.penup()
turtle.goto(150,250)
turtle.pendown()
turtle.setheading(90)
turtle.forward(20)
turtle.penup()
turtle.goto(170,240)
turtle.pendown()
turtle.setheading(90)
turtle.forward(40)

#Draw the big tree
turtle.penup()
turtle.goto(500,-100)
turtle.pendown()
Rectangle.drawRectangle(turtle, 100, 50, "grey")
turtle.penup()
turtle.goto(415,0)
turtle.pendown()
turtle.setheading(0)
Triangle.drawTriangle(turtle, 120, "green")
turtle.penup()
turtle.goto(425,60)
turtle.pendown()
Triangle.drawTriangle(turtle, 100, "green")
turtle.penup()
turtle.goto(435,110)
turtle.pendown()
Triangle.drawTriangle(turtle, 80, "green")
#Draw the small tree
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
Rectangle.drawRectangle(turtle, 30, 80, "grey")
turtle.penup()
turtle.goto(-120,-20)
turtle.pendown()
turtle.setheading(0)
Triangle.drawTriangle(turtle, 70, "green")
turtle.penup()
turtle.goto(-110,15)
turtle.pendown()
turtle.setheading(0)
Triangle.drawTriangle(turtle, 50, "green")
turtle.penup()
turtle.goto(-100,40)
turtle.pendown()
turtle.setheading(0)
Triangle.drawTriangle(turtle, 30, "green")

#Draw the sun
turtle.penup()
turtle.goto(400,400)
turtle.setheading(0)
turtle.pendown()
for i in range (4):
    turtle.left(45)
    turtle.forward(80)
    turtle.goto(400,400)
    turtle.left(45)
    turtle.forward(100)
    turtle.goto(400,400)
turtle.penup()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(400,350)
turtle.pendown()
turtle.circle(50)
turtle.end_fill()
#Draw the cloud
turtle.penup()
turtle.goto(400,300)
turtle.setheading(0)
turtle.pendown()
cloud.drawcloud(turtle, 100, 180, "white")
turtle.penup()
turtle.goto(350,250)
turtle.setheading(0)
turtle.pendown()
cloud.drawcloud(turtle, 100, 180, "white")

turtle.penup()
turtle.goto(150,-100)
turtle.setheading(90)
turtle.done()