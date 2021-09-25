import turtle
pen = turtle.Turtle()
from Class_rectangle import rectangle
rectangle01 = rectangle(long = 200,width= 300)
rectangle02 = rectangle(long = 300,width= 100)

print(f'Rectangle Infor \n{rectangle01}')
rectangle01.draw_rectangle(pen)
rectangle02.draw_rectangle(pen)
turtle.done()


