import turtle
import random

number = random.uniform(0, 3)
intNumber = int(number)
turtle.title("number is:" + str(number) + ". intNumber is:" + str(intNumber))
ball = turtle.Turtle()
ball.shapesize(10)
ball.shape('circle')
if intNumber < 1:
    ball.color('green')
elif intNumber < 2:
    ball.color('yellow')
elif intNumber < 3:
    ball.color('red')
turtle.done()