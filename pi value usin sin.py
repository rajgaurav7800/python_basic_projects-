import math
while (1):
    n = float(input("enter the aproximation = "))
    cer = n * math.sin(math.radians(180) / n)
    dia = 1
    print("value of pi =", float(cer / dia))
    print("\n\n")
# 3.141592653589793238462643383279
# 3.141592653589793