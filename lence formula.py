while (1):
    t = input("(a)concave mirror..)\n(b)convex mirror..(\n(c)concave lens..)(\n(d)convex lens..()\nenter your choice...")
    if t == "a":
        u = float(input("distence from mirror..."))
        f = float(input("focus of mirror..."))
        v = ((-f) * (-u)) / ((-u) - (-f))
        print("V=", v)
        m = -(v) / (-u)
        print("M=", m)
        if m > 1:
            print("image is magnified/inlarged")
        elif m < 1:
            print("image is dimnised/small")
        if v > 0:
            print("image is virtual and erect ")
        elif v < 0:
            print("image is real and inverted\n\n\n")
    elif t == "b":
        u = float(input("distence from mirror..."))
        f = float(input("focus of mirror..."))
        v = ((f) * (-u)) / ((-u) - (f))
        print("V=", v)
        m = -(v) / (-u)
        print("M=", m)
        if m > 1:
            print("image is magnified/inlarged")
        elif m < 1:
            print("image is dimnised/small")
        if v > 0:
            print("image is virtual and erect ")
        elif v < 0:
            print("image is real and inverted\n\n\n")
    elif t == "c":
        u = float(input("distence from lens..."))
        f = float(input("focus of lens..."))
        v = ((-f)*(-u)) / ((-u) + (-f))
        print("V=", v)
        m = (v) / (-u)
        print("M=", m)
        if m > 1:
            print("image is magnified/inlarged")
        elif m < 1:
            print("image is dimnised/small")
        if v < 0:
            print("image is virtual and erect ")
        elif v > 0:
            print("image is real and inverted\n\n\n")
    elif t == "d":
        u = float(input("distence from lens..."))
        f = float(input("focus of lens..."))
        v = ((f) * (-u)) / ((-u) - (f))
        print("V=", v)
        m = (v) / (-u)
        print("M=", m)
        if m>1:
            print("image is magnified/inlarged")
        elif m<1:
            print("image is dimnised/small")
        if v < 0:
            print("image is virtual and erect ")
        elif v > 0:
            print("image is real and inverted\n\n\n")