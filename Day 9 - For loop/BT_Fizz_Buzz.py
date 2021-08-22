a = int(input("Nhap a:"))
b= int(input("Nhap b:"))

for i in range(a, b+1):
    if i % 15 == 0:
        print(str(i) + "-FizzBuzz")
    elif i % 3 == 0:
        print(str(i) + "-Fizz")
    elif i % 5 == 0:
        print(str(i) + "-Buzz")
    else:
        print(i)
    i += 1