while(1==1):
    a1 = int(input("a1..."))
    b1 = int(input("b1..."))
    c1 = int(input("c1..."))
    a2 = int(input("a2..."))
    b2 = int(input("b2..."))
    c2 = int(input("c2..."))
    if ((a1 / a2) != (b1 / b2)):
        print("intersecting (x)")
    elif ((a1 / a2) == (b1 / b2) != (c1 / c2)):
        print("parallel (==)")
    elif ((a1 / a2) == (b1 / b2) == (c1/c2)):
        print("overlapping (--)")
    x = ((b1 * c2) - (b2 * c1)) / ((a1 * b2) - (a2 * b1))
    y = ((c1 * a2) - (c2 * a1)) / ((a1 * b2) - (a2 * b1))
    print("x=", x, "y=", y)
