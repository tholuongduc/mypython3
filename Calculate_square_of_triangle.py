import math

a = float(input("Enter the length of side a:"))
b = float(input("Enter the length of side b:"))
c = float(input("Enter the length of side c:"))

#Peripheral
s = (a+b+c)/2
#Square
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of the triangle is:", area)
