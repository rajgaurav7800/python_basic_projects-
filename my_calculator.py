while 1:
    o = input("what u want to perform (+)(-)(*)(/)...")
    x = (input("enter your first no...."))
    y = (input("enter your second no...."))
    if o=="-":
        print("0")
    elif o=="*":
        print(int(x)*y)
    elif o=="/":
        print(int(x)/int(y))
    else:
        print(str(x)+str(y))
