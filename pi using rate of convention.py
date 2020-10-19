while (1):
    x = 1
    t = int(input("value of times = "))
    v = 4 / x
    x = x + 2
    while (1):
        v = v - (4 / x)
        x = x + 2
        v = v + (4 / x)
        x = x + 2
        t = t + 1
        print(v, t)

#   =3.141592653589793238462643383279
#ans=3.14165335898645