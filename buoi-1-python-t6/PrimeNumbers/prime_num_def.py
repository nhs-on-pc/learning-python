def print_prime(n: int):
    if 3 <= n:
        for num in range(1, 3):
            print(num, end=", ")


    for num in range(3, n + 1):
        isPrime = True
        for i in range(2, num//2 + 1):
            if num % i == 0:
                isPrime = False
                break

        if isPrime:
            print(num, end=", ")


print_prime(7)