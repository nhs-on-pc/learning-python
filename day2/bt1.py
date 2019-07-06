def giaithua(n: int):
    multiply = 1
    for i in range(2, n+1):
        multiply = multiply * i
    print(multiply)


giaithua(3)
