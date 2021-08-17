#Xac dinh tam giac
a = float(input("Hay nhap canh a:"))
b = float(input("Hay nhap canh b:"))
c = float(input("Hay nhap canh c:"))

if a <= 0 or b <= 0 or c <= 0:
    print("Canh cua tam giac phai la so nguyen duong")
else:
    if a + b > c and a + c > b and b + c > a:
       if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
           print("Day la tam giac vuong")
       elif a == b and b == c:
           print("Day la tam giac deu")
       elif a == b or b == c or c == a:
           print("Day la tam giac can")
       elif a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b:
           print("Day la tam giac tu")
       else:
           print("Day la tam giac nhon")
    else:
        print(str(a) + "," + str(b) + "," + str(c) + " khong la 3 canh cua tam giac")