# prime number
i = int(input("Nhập i: "))
for i in range(4, i + 1):
    isPrime = True
    for j in range(2, i//2 + 1):
        if i % j == 0:
            isPrime = False
            break
        if i % j != 0:
            continue
    if isPrime is True:
        print(i)

