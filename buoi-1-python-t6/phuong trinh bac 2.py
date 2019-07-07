def ptb2(a: float, b: float, c: float):
    if a <= 0 and (b, c) < 0:
        print("Nhap lai a, b, c")
    else:
        delta = b*b - 4*a*c

        if delta < 0:
            #print(-delta**(1/2))
            x1 = complex(-b/(2*a), -(-delta**(1/2))/(2*a))
            x2 = complex(-b/(2*a), +(-delta**(1/2))/(2*a))
            print("Phuong trinh co hai nghiem phuc phan biet: ", x1, x2)

        elif delta == 0:
            x = round(-b/(2*a), 3)
            print("Nghiem kep cua phuong trinh la: ", x)
        else:
            x3 = round((-b - delta**(1/2))/(2*a), 3)
            x4 = round((-b + delta**(1/2))/(2*a), 3)
            print("Phuong trinh co hai nghiem: ", x3, x4)

ptb2(1, 3, -2)