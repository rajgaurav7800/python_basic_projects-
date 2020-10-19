import pyautogui,time
pyautogui.FAILSAFE=True
def move(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
def type(x):
    pyautogui.typewrite(x)
def delay(x):
    time.sleep(x)
pyautogui.hotkey("winleft","r")
move(217, 665)
type("\b\b\b\b\b\b\b\b\b\bcmd\n")
delay(2)
pyautogui.hotkey("winleft","up")
# while 1:
#     for i in range(10):
#         type(f"color {i}\ncolor z\n")
#         print(f"color {i}")
type("python\n")
type("import random\nwhile 1:\n\tx=random.randint(0,9)\n\tprint(x,end='')\n\n")
# type("import time\nfor i in range(24):\n\tfor j in range(60):\n\t\tfor k in range(60):\n\t\t\tprint(f'time = {i}:{j}:{k}')\n\t\t\ttime.sleep(1)\n\n")

