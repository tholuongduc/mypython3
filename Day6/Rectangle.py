import turtle
#Define a function to draw front side (rectangle)
def drawRectangle (t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()