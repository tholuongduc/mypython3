en_dict = {
    "French": "Nước Pháp, người Pháp",
    "Vietnamese": "Người Việt Nam",
    "England": "Nước Anh, người Anh"
}
#Show menu
def show_menu():
    print('''Please select program mode:
        1) Show all word
        2) Search word
        3) Exit program!
          ''')
#Select program mode
def get_choice():
    return input("Please select mode: ")

#hiển thị dữ liệu
def show_all(en_dict):
    en_dict_itor = iter(en_dict)
    while True:
        try:
            key = next(en_dict_itor)
            print(f'{key:<10}:{en_dict.get(key)}')
        except StopIteration:
            break

#Tra tu
def search(en_dict):
    while True:
        search_name = input("Please enter contact name:").lower().capitalize()
        if search_name in en_dict.keys():
            print(search_name, ":", en_dict.get(search_name))
            break
        else:
            print(search_name, " is not in contact book. Please enter name correctly!")
            continue

#main
while True:
    show_menu()
    user_choice = get_choice()
    print("You select mode: " + user_choice)

    if user_choice == "3":
        break
    elif user_choice == "1":
        show_all(en_dict)
    elif user_choice == "2":
        search(en_dict)
    else:
        print("Invalid mode!Try again!")
