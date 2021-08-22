#Viết ứng dụng cho phép nhập vào 1 số nguyên dương (>=2) và xác định số đó có phải là số nguyên tố hay không
import math

while True:
    a = input("Hãy nhập số bạn cần kiểm tra:")
    if a.isdigit() and int(a) == 2:            #Kiểm tra ký tự nhập vào có phải là dạng số nguyên dương và = 2
        print(a + " là số nguyên tố.")
        break
    elif a.isdigit() and int(a) > 2:           #Kiểm tra ký tự nhập vào có phải là dạng số nguyên dương và > 2
        a = int(a)
        for i in range (2, a):                 #Vòng lặp kiểm tra tính nguyên tố
            b = a % i
            while b == 0:
                print(str(a) + " không là số nguyên tố.")
                exit()
        print(str(a) + " là số nguyên tố.")
        exit()
    else:                                     # Yêu cầu nhập lại sô cần kiểm tra
        print("Hãy nhập số nguyên dương >= 2!")
