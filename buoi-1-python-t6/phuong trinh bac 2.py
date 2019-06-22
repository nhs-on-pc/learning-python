def ptb2(a: float, b: float, c: float) -> (float, float):

    a = int(input("Nhap a:"))
    b = int(input("Nhap b:"))
    c = int(input("Nhap c:"))

    delta = b**b - 4*a*c

    if delta < 0:
        print("Phuong trinh vo nghiem")
    if delta == 0:
        x = -b/2*a
        print("Nghiem cua phuong trinh la: ", x)
    if delta > 0:
        x1 = (-b - delta**1/2)/2*a
        x2 = (-b + delta**1/2)/2*a
        print("Nghiem kep cua phuong trinh la: ", x1, x2)