x = input("enter a no...")
l = len(x)
nu = 0
t = 0
while l!=0:
    t = t + int(x[nu])
    nu += 1
    l = l - 1
print(t)