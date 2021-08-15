import turtle
#Define a function to draw a cloud
def drawcloud (t, radius, angle, color):
    t.fillcolor(color)
    t.begin_fill()
    turtle.forward(radius * 2)
    turtle.left(90)
    turtle.circle(radius * 2 / 3, angle)
    turtle.setheading(90)
    turtle.circle(radius / 3, angle)
    turtle.end_fill()