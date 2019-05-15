n = 99
while n > 0:

    print(n, "bottles of beer on the wall")
    print(n, "bottles of beer")
    print("Take one down, pass it around")
    print(n-1, "bottles of beer on the wall\n")

    if n == 1:
        break
    n -= 1