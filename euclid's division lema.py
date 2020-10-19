x = int(input("a="))
y = int(input("b="))
a = x
b = y
q = a//b
r = a % b
# print(a, "=", b, "*", q, "+", r)
while r != 0:
    a = b
    b = r
    q = a // b
    r = a % b
    print(a, "=", b, "*", q, "+", r)
print("HCF=",b)
print("LCM=", ((x*y)/b))