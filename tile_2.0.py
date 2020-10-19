import pyautogui   
from PIL import ImageGrab
# from PIL import image
import time
pyautogui.FAILSAFE = True
input("\nmove the mouse to set x, y for p1\nand press enter...")
p_1 = pyautogui.position()
p1_x = p_1[0]
p1_y = p_1[1]
input("\nmove the mouse to set x, y for p2\nand press enter...")
p_2 = pyautogui.position()
p2_x = p_2[0]
p2_y = p_2[1]
input("\nmove the mouse to set x, y for p3\nand press enter...")
p_3 = pyautogui.position()
p3_x = p_3[0]
p3_y = p_3[1]
input("\nmove the mouse to set x, y for p4\nand press enter...")
p_4 = pyautogui.position()
p4_x = p_4[0]
p4_y = p_4[1]
a = 70
dis = 30


def movec(p):
    if p == 1:
        pyautogui.moveTo(p1_x, p1_y+dis)
        pyautogui.click()
        # print("clicking--->p1")
        return
    elif p == 2:
        pyautogui.moveTo(p2_x, p2_y+dis)
        pyautogui.click()
        # print("clicking--->p2")
        return
    elif p == 3:
        pyautogui.moveTo(p3_x, p3_y+dis)
        pyautogui.click()
        # print("clicking--->p3")
        return
    elif p == 4:
        pyautogui.moveTo(p4_x, p4_y+dis)
        pyautogui.click()
        # print("clicking--->p4")
        return


def p1(q):
    x = p1_x
    y = p1_y
    for i in range(x, x+30):
        for j in range(y, y+30):
            if q[i, j] < a:
                movec(1)
                # print("p1 ---> true")
                return


def p2(q):
    x = p2_x
    y = p2_y
    for i in range(x, x+30):
        for j in range(y, y+30):
            if q[i, j] < a:
                movec(2)
                # print("p2 ---> true")
                return


def p3(q):
    x = p3_x
    y = p3_y
    for i in range(x, x+30):
        for j in range(y, y+30):
            if q[i, j] < a:
                movec(3)
                # print("p3 ---> true")
                return


def p4(q):
    x = p4_x
    y = p4_y
    for i in range(x, x+30):
        for j in range(y, y+30):
            if q[i, j] < a:
                movec(4)
                # print("p4 ---> true")
                return


print("start in 2")
time.sleep(1)
print("start in 1")
time.sleep(1)
print("start in 0...started    ")
while 1:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    p1(data)
    p2(data)
    p3(data)
    p4(data)
    # x = p1_x
    # y = p1_y
    # for u in range(x, x+30):
    #     for v in range(y, y+30):
    #         data[u, v] = 120
    # image.show()
    # break
