  times = int(input("enter acuracy = "))
    x = 2
    q = 3 + (4 / (x * (x + 1) * (x + 2)))
    x = x + 2
    while times != 0:
        q = q - (4 / (x * (x + 1) * (x + 2)))
        x = x + 2
        q = q + (4 / (x * (x + 1) * (x + 2)))
        x = x + 2
        times = times - 1
    print("value of pi = ", float(q))
    print("\n")

# t = 0
# x = 2
# q = 3 + (4 / (x * (x + 1) * (x + 2)))
# x = x + 2
# while (q!=3.1415926535897932):
#     q = q - (4 / (x * (x + 1) * (x + 2)))
#     x = x + 2
#     q = q + (4 / (x * (x + 1) * (x + 2)))
#     x = x + 2
#     t = t + 1
#     print("value of pi = ", float(q),  t)


#    3.141592653589793238462643383279
#p1= 3.141592653589793
#=== 3.141592653589787