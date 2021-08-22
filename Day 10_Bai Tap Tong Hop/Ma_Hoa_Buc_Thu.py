#Vị Giám đốc công ty XYZ cần gửi một văn bản quan trọng tới đối tác. Để bảo mật văn bản, GĐ quyết định mã hóa văn bản trước khi gửi. Văn bản là một chuỗi S. Ông ta chia văn bản thành hai đoạn liên tiếp Sb và Se. Lần lượt viết hai chuỗi Sb và Se theo thứ tự ngược lại. Kết quả được chuỗi mã hóa Q. Để đọc được văn bản, chúng ta cần biết khóa để giải mã: đó là độ dài k của chuỗi Sb.
#Yêu cầu: Viết chương trình mã hóa và giải mã một chuỗi nội dung.
#Đầu vào
#● Chọn chức năng: mã hóa hoặc giải mã (có thể chọn bằng số)
#● Nhập vào chuỗi mã hóa Q (hoặc văn bản S) có độ dài từ 1 đến 1000
#● Nhập vào khóa k
#Kết quả:
#● Nếu người dùng chọn chức năng mã hóa, hiển thị chuỗi mã hóa.
#● Nếu người dùng chọn chức năng giải mã, hiển thị văn bản gốc.
#Ví dụ: Nội dung bức thư S = 'programming' được chia thành 2 đoạn: Sb = 'program', Se = 'ming', nhận được xâu mã
#hóa Q = ’margorpgnim’ với khóa k = 7.

#Nhập đoạn văn bản
s = input("Hãy nhập đoạn văn bản của bạn:")
length_s = len(s)
key = input("Hãy nhập key:")
#Bạn muốn mã hóa hay giải mã? Mã hóa = 0, Giải mã = 1
mode = input("Bạn muốn mã hóa hay giải mã? Mã hóa chọn 0, Giải mã chọn 1:")

if mode == '0':
    while True:
        if key.isdigit() and int(key) <= length_s:
            print("Bạn đã chọn chức năng mã hóa. Đang mã hóa văn bản, xin vui lòng đợi trong giây lát!")
            break
        else:
            print("Key không hợp lệ!")
            key = input("Hãy nhập số nguyên từ 1 đến " + str(length_s) + ":")
            continue
    key = int(key)
    sb = str(s[0:key])
    se = str(s[key:length_s + 1])
    bs = sb[::-1]
    es = se[::-1]
    Q = bs + es
    print("Đã mã hóa thành công! Đoạn văn bản được mã hóa là:\n" + Q)
elif mode == '1':
    print("Bạn đã chọn chức năng giải mã. Đang giải mã văn bản, xin vui lòng đợi trong giây lát!")
    key = int(key)
    sb = str(s[0:key])
    se = str(s[key:length_s + 1])
    bs = sb[::-1]
    es = se[::-1]
    Q = bs + es
    print("Đã giải mã thành công! Đoạn văn bản gốc là:\n" + Q)
else:
    print("Bạn chưa chọn đúng chức năng. Hãy chọn lại!")








