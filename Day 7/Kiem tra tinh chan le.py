a = input("Enter your number:")
a = float(a)

if a % 2 == 0:
    print(str(a) + " is even")
elif a % 2 == 1:
    print(str(a) + " is odd")
else:
    print(str(a) + " is not integer")