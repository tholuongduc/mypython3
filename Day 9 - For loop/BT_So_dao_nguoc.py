#Viết chương trình cho phép nhập vào 1 số nguyên dương và in ra màn hình số đảo ngược của nó
#Note: chỉ được sủ dụng toán tử và vòng lặp, không sử dụng phương pháp index với chuỗi
a = input("Hay nhap a:")
if a.isdigit():
    a = int(a)
    while a != 0:
        print(a % 10, end = "")
        a = a // 10
else:
    print("a phai la so nguyen")