import pyautogui
import time
def hit(key):
    pyautogui.keyDown(key)
time.sleep(1)
print('start in 3_sec')
time.sleep(1)
print('start in 2_sec')
time.sleep(1)
print('start in 1_sec')

while 1:
    hit("R")
    hit("A")
    hit("J")
    hit("space")
    hit("G")
    hit("A")
    hit("U")
    hit("R")
    hit("A")
    hit("V")
    hit("space")


0