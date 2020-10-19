while(1):
    import random

    times = int(input('times...'))
    u = times
    x = int(0)
    z = 0
    while (u != 0):
        y = random.random()
        y = int(10 * float(y))
        if y < 5:
            # print(int(0))
            x = x + 1
        else:
            # print(int(1))
            z = z + 1
        u = u - 1
    print(x / times)