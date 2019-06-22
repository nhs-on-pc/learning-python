def fibo(n: int) -> int:
    if n <= 1:
        return n
    else:
        a_i_2 = 0
        a_i_1 = 1
        for i in range(2, n+ 1):
            a = a_i_2 + a_i_1
            a_i_2 = a_i_1
            a_i_1 = a
        return a