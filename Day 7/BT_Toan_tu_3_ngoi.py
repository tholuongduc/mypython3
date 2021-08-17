#Kiem tra tinh chan le cua gia tri nhap vao
number = float(input("Enter your number:"))

msg = "Even" if number % 2 == 0 else "Odd" if number % 2 == 1 else "not Integer"
print(str(number) + " is " + msg)