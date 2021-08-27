#[Bài tập*] Tìm số trong một dãy số
#Một sinh viên trường đại học A đang nghiên cứu về các dãy số. Thời gian vừa qua, anh ta
#cần phải giải quyết một bài toán khá thú vị liên quan tới số aN của dãy a0, a1, a2, ..., trong đó:
#● a0 = 0
#● ai là số nguyên dương nhỏ nhất lớn hơn ai-1
#● ai không chứa các chữ số đã tồn tại trong ai-1 với i ≥ 1

#Define function to find the number satisfying the condition
def generate(number):
    my_string = "0123456789"
    convert_number = str(number)
    result = ""
    for i in range(len(convert_number)):
        my_string = my_string.replace(convert_number[i],"")
    #print(my_string)
    for i in range(len(my_string)):
        if my_string[i] > convert_number:
            result = my_string[i] + my_string[0] * (len(convert_number) - 1)
            break
    else:
        if my_string[0] != "0":
            result = my_string[0] * (len(convert_number) + 1)
        else:
            result = my_string[1] + my_string[0] * len(convert_number)

    return result

#List N number
N = int(input("Please enter possition of your number:"))
count = 0
string = ""
while True:
    print(f"{generate(string)}", end=" ")
    string = generate(string)
    if count == N:
        break
    else:
        count = count + 1
print("\n----------------------------------\n")
print("Your number is: " + string)