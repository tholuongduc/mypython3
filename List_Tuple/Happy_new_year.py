friends = ["Hoa", "Hang", "The Anh", "Huong", "Dieu", "Lien"]

your_string = "Happy new year,"

def congrats(list, your_string):
    for name in list:
        print(your_string + name)


final_greeting = congrats(friends,your_string)

