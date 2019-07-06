def fibo(n: int):
    fibo = [0, 1]
    for i in range(2, n):
        fibonext = fibo[i-1] + fibo[i-2]
        fibo.append(fibonext)
        print(fibo)


fibo(10)
