#define a funtion to check prime number
def find_prime_number(lst):
    prime_list = []
    for i in lst:
        for j in range(2, i // 2 +1):
            b = i % j
            if b == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

#main
numbers_list_1 = [1, 10, 5, 2, 8, 7, 13, 121, 79]
prime_list = find_prime_number(numbers_list_1)
print(prime_list)