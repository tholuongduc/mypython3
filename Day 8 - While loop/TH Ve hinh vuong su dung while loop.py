#draw a square using while loop
import turtle
#Declare width of square
a = int(input("Enter width of square:"))

i = 0
while i < 4:
    turtle.forward(a)
    turtle.left(90)
    i += 1
else:
    print("Completed!")
turtle.done()