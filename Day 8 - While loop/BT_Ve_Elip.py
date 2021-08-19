import turtle
import random
color_list = ["red", "yellow", "orange", "green", "blue", "gray", "violet"]
#Xay dung ham ve elip
def drawelip (t, radius, color):
    i = 0
    t.pencolor(color)
    t.pensize(5)
    t.speed(20)
    while i < 2:
        t.circle(radius, 90)
        t.circle(radius / 2, 90)
        i += 1
#Ve nhieu hinh elip
a = int(input("Hay nhap so vong ban muon ve:"))
j = 0
while j < a:
    t = turtle.Turtle()
    color = random.choice(color_list)
    drawelip(turtle, 100, color)
    turtle.left(360 / a)
    j += 1
turtle.done()







