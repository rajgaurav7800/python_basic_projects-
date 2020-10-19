import random


def digitalsum(q):
    temp = 0
    while 1:
        q = str(q)
        for i in q:
            temp += int(i)
        if len(q) == 1:
            return int(q)
            # break
        q = int(temp)
        temp = 0


while 1:
    x = random.randint(10, 1000)
    print(f"the digital sum of {x} = ", end="")
    t = input()
    if int(t) == digitalsum(x):
        continue
    else:
        print("ans", digitalsum(x))
        break
# print(digitalsum(125))
