import pyautogui as pag
import time
pag.FAILSAFE = True


def typ(x):
    pag.typewrite(x)
    # print(x,end="")


def check(x):
    x = str(x)
    x = len(x)
    if x == 1:
        return True  # if x is a once
    else:
        return False  # if x is tens


for i in range(24):
    if check(i):
        typ(f"0{i}:")
    else:
        typ(f"{i}:")
    for j in range(60):
        if check(j):
            typ(f"0{j}:")
        else:
            typ(f"{j}:")
        for k in range(60):
            if check(k):
                typ(f"0{k}")
            else:
                typ(f"{k}")
            time.sleep(0.95)
            typ("\b\b")
        typ("\b\b\b")
    typ("\b\b\b")
