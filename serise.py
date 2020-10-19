

def tolist(q):
    temp = []
    if type(q) == str:

        for yi in q:
            temp.append(yi)
    else:

        q = str(q)
        for yi in q:
            temp.append(yi)
    return temp


def toint(q):
    temp = ""
    if type(q) == list:
        for yi in q:
            temp += str(yi)
    else:
        temp = int(q)
    temp = int(temp)
    return temp


def straight(q):
    lis = tolist(q)
    lis.sort()
    lis = toint(lis)
    return lis


def revers(q):
    q = tolist(q)
    q.sort()
    temp = q[::-1]
    temp = toint(temp)
    return temp


time = false = true = 0
x = 1000
for i in range(x, 100000):
    x = i
    while x != 6174:
        if time == 9:
            time = 0
            break
        elif straight(x) > revers(x):
            # print(f"{straight(x)} - {revers(x)} = {straight(x) - revers(x)}")
            x = straight(x) - revers(x)
        else:
            # print(f"{revers(x)} - {straight(x)} = {revers(x) - straight(x)}")
            x = revers(x) - straight(x)
        time += 1
    if x == 6174:
        # print(f"--------------------true = {i}")
        true += 1
    else:
        # print(f"--------------------false = {i}")
        false += 1
print(f"true = {true}\nfalse = {false}\ntrue + false = {true + false}")
# 5482
