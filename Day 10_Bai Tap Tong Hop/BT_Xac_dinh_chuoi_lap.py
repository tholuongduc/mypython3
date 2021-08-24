#Trong giờ thực hành soạn thảo văn bản trên MS Word, mỗi sinh viên cần gõ một chuỗi kí tự bất
#kì. Khi xem xét chuỗi kết quả của sinh viên, giáo viên phát hiện ra rằng có một số chuỗi lặp đặc
#biệt được tạo thành bằng cách ghép k lần một chuỗi con (k > 1). Ví dụ, ’ABABAB’ là một chuỗi
#đặc biệt, lặp lại 3 lần chuỗi con ’AB’.
#Hãy viết chương trình hỗ trợ giáo viên kiểm tra xem một chuỗi nhập vào có phải là chuỗi lặp haykhông.
#Ví dụ:
#● Đầu vào: ABABAB
#● Đầu ra: “ABABAB” là chuỗi lặp
#● Đầu vào: ABA1BAB
#● Đầu vào: “ABA1BAB” không phải là chuỗi lặp

#Nhập chuỗi
s = input("Hãy nhập chuỗi ký tự của bạn:")
length_s = len(s)

for i in range (1, length_s // 2 + 1):
    sb = str(s[0:i])
    length_sb = len(sb)
    j = length_s / i
#    se = str(s[i:i + length_sb])
    if j.is_integer():
        se = sb * int(j)
        if s == se:
            print(s + " là chuỗi lặp của " + sb + ".")
            exit()
        else:
            continue
    else:
        continue
print(s + " không là chuỗi lặp.")