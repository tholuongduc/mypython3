import turtle
import math

r = int(input("Enter the radius:"))

turtle.hideturtle()
turtle.circle(r)
turtle.done()

c = 2 * math.pi * r
s = math.pi * r * r

print("Chu vi của hình tròn có bán kính = {r} là {c}".format(r=r, c=c))
print("Diện tích của hình tròn có bán kính = {r} là {s}".format(r=r, s=s))