import turtle
turtle.speed(20)
turtle.pensize (5)
turtle.pencolor ("black")

#Face
pace_size = 100
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle (pace_size)
turtle.end_fill()

#Eyes
eyes_size = 20
turtle.penup()
turtle.goto(-40,110)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle(eyes_size)
turtle.penup()
turtle.goto(40,110)
turtle.pendown()
turtle.circle(eyes_size)
turtle.end_fill()

#Mount
turtle.penup()
turtle.goto(-40,50)
turtle.pendown()
turtle.right(45)
turtle.circle(60,100)


#Nose
turtle.penup()
turtle.goto(0,80)
turtle.pendown()
turtle.setheading(0)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(-10, steps=3)
turtle.end_fill()

turtle.done()