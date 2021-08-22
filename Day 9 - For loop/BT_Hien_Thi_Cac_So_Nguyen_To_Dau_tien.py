#Viết chương trình xác số nguyên tố. Cho phép nhập vào 1 số nguyên dương n (n >0) và hiển thị n số nguyên tố đầu tiên
import math

n = int(input("Hãy nhập n số nguyên tố đầu tiên bạn muốn xem:"))
count = 0
i = 0 #Khai báo số để kiểm tra tính nguyên tố
while count < n:
    i += 1 #Kiểm tra từ 1
    for j in range(2, i // 2 + 1):  #Vòng lặp kiểm tra tính nguyên tố
        if i % j == 0:
            break
    else:
        print(i, end=" ")  #In ra số nếu số đó là số nguyên tố
        count += 1





