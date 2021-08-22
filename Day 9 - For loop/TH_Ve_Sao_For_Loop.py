#Ve sao = for loop
import turtle

turtle.bgcolor("black")
turtle.title("Start")

#khai bao ham ve star
def drawStart (t, lenght, angle, color):
    t.pencolor(color)
    t.speed(20)
    for i in range (1, 6):
        t.left(angle)
        t.forward(lenght)


for j in range (1, 73):
    drawStart(turtle, 200, 144, "red")
    turtle.left(5)
turtle.done()