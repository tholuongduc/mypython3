char = input('Your char?: ')
width = int(input('Width?: '))
height = int(input('Height?: '))

for i in range(1, height + 1):
    print_str = ''
    for j in range(1, width + 1):
        if i == 1 or i == height:
            print_str += char
        else:
            if j == 1 or j == width:
                print_str += char
            else:
                print_str += ' '
    print(print_str)