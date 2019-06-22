def pi(n: int) -> float:
    i = 1
    heso = 1
    sum = 0
    for i in range(1, n):

        sum = 4*(heso*1/(2*i-1))
        heso = -heso
        print(sum)
        #sum = 1/(2*i-1) + heso*1/(2*(i+1)-1)

pi(10)