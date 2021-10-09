import turtle as tt
import time

t = tt.Turtle()
t.color("blue")
screen = tt.Screen()
screen.tracer(0)
t.hideturtle()

#Define draw function
def draw_rectangle(pen, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.down()
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)

#define print text function
def draw_text(pen, x, y, text):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.write(text, font=("Arial", 30, "normal"))

def notify_collision(rect1, rect2):
    if is_collision(rect1, rect2):
        draw_text(t, 0, 200, "Collision Occurs!")
    else:
        draw_text(t, 0, 200, "Rect2 is moving")

#define checking collision
def is_collision(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    return x1 + w1 >= x2 and x1 <= x2 + w2 and y1 + h1 >= y2 and y1 <= y2 + h2

x1 = -10
y1 = -200
w1 = 100
h1 = 50

x2 = -300
y2 = -200
w2 = 100
h2 = 50

def move():
    draw_rectangle(t, x1, y1, w1, h1)
    draw_rectangle(t, x2, y2, w2, h2)

    rect1 = (x1, y1, w1, h1)
    rect2 = (x2, y2, w2, h2)
    notify_collision(rect1, rect2)
    screen.update()

def move_up():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    y2 += 5
    move()
def move_down():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    y2 -= 5
    move()
def move_right():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    x2 += 5
    move()
def move_left():
    global x1, y1, w1, h1, x2, y2, w2, h2
    t.clear()
    x2 -= 5
    move()

tt.onkeypress(move_up, "Up")
tt.onkeypress(move_down, "Down")
tt.onkeypress(move_left, "Left")
tt.onkeypress(move_right, "Right")
tt.listen()
tt.done()