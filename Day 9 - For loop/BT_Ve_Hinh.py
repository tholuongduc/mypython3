#Dùng ký tự vẽ hình theo yêu cầu
char = input('Your char?: ')
length = int(input('Length?: '))

#Hình số 1
#for i in range(1, int(length)):
#    print(char * i)

#Hình số 2
#for i in range(int(length), 0, -1):
#    print(char * i)

#Hình số 3
#for i in range(int(length), 0, -1):
#    print(i*" " + char * (int(length) + 1 -i))

#Hình số 4
for i in range(1,int(length)+1):
    print(i*" " + char * (int(length) + 1 -i))
