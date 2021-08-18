import turtle
import random

#Racer 1
racer_1 = turtle.Turtle()
racer_1.shape("turtle")
racer_1.pencolor("red")
racer_1.hideturtle()
racer_1.penup()
racer_1.speed(5)
#Racer 2
racer_2 = racer_1.clone()
racer_2.shape("turtle")
racer_2.pencolor("blue")
racer_2.hideturtle()
racer_2.penup()
racer_2.speed(5)
#The finish line
racer_1.goto(500, 0)
racer_1.pendown()
racer_1.circle(5)
racer_2.goto(500, -50)
racer_2.pendown()
racer_2.circle(5)

#Back to start point:
racer_1.penup()
racer_1.goto(-500, 0)
racer_1.showturtle()
racer_2.penup()
racer_2.goto(-500, -50)
racer_2.showturtle()

#Start racing
i = 0
while i < 30:
    if racer_1.pos() >= (500,0):
        print("Congrats!Turtle 1 is winner!")
        break
    elif racer_2.pos() >= (500,-50):
        print("Congrats!Turtle 2 is winner!")
        break
    else:
        a = random.randint(20, 50)
        b = random.randint(20, 50)
        c = random.randint(20, 50)
        d = random.randint(20, 50)
        racer_1.pendown()
        racer_1.forward(a)
        racer_1.penup()
        racer_1.forward(b)
        racer_2.pendown()
        racer_2.forward(c)
        racer_2.penup()
        racer_2.forward(d)
        i += 1
else:
    print("No one is winner!")
turtle.done()
