def pi_number(n: int) -> float:
    heso = []
    pi = 0
    tong = 0
    for i in range(n):
        if i % 2 == 0:
            heso.append(1)
        else:
            heso.append(-1)
        tong = tong + heso[i]*1/(2*i+1)
    pi = 4 * tong
    print(pi)


pi_number(1000000)
