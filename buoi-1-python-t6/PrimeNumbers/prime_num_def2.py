import math


def print_prime(n: int) -> [int]:
    prime_list = [1, 2, 3]

    for num in range(4, n + 1):
        is_prime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(num)

    return prime_list

# Cách này dùng mảng các số nguyên tố trước đó để thử
def print_prime2(n: int) -> [int]:
    prime_list = [1, 2, 3]

    for num in range(5, n + 1):
        is_prime = True
        i = 1

        while prime_list[i] < num//2 + 1:
            if num % prime_list[i] == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            prime_list.append(num)

    return prime_list


def print_prime3(n: int) -> [int]:
    prime_list = [1, 2, 3]

    for num in range(5, n + 1):
        is_prime = True
        i = 1
        half_num = num//2 + 1
        a_prime = prime_list[i]
        while a_prime < half_num:
            if num % a_prime == 0:
                is_prime = False
                break
            i += 1
            a_prime = prime_list[i]

        if is_prime:
            prime_list.append(num)

    return prime_list

def print_prime4(n: int) -> [int]:
    prime_list = [1, 2, 3]

    for num in range(5, n + 1):
        is_prime = True
        i = 1
        half_num = int(math.sqrt(num)) + 1
        a_prime = prime_list[i]
        while a_prime < half_num:
            if num % a_prime == 0:
                is_prime = False
                break
            i += 1
            a_prime = prime_list[i]

        if is_prime:
            prime_list.append(num)

    return prime_list

N = 10000
from time import time

start = time()
prime_list = print_prime(N)
delta = (time()-start)
print(delta)


start = time()
prime_list2 = print_prime2(N)
delta = (time()-start)
print(delta)

start = time()
prime_list3 = print_prime3(N)
delta = (time()-start)
print(delta)

start = time()
prime_list4 = print_prime4(N)
delta = (time()-start)
print(delta)



if prime_list2 != prime_list4:
    print("Kết quả 2 cách là khác nhau")
else:
    print("Kết quả 2 cách là giống nhau")
