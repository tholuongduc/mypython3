#Tinh nam am lich tu nam duong lich
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh','Mậu','Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']

condition = False
while (condition == False):
    year = int(input("Enter year:"))
    if year <= 0:
        print("Invalid!Please try again (year > 0):")
    else:
        condition = True
        index_can = year % 10
        index_chi = year % 12
        print(str(year) + " is: " + can[index_can] + " " + chi[index_chi])