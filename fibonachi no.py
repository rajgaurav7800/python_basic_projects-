print("0  1",end="  ")

a = 0
b = 1
c = 0
for i in range(100):
    a = b
    b = c
    c = a + b
    print(c, " ",end="")
