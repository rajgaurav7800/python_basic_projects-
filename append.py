import random
import pyautogui
x=[]
print('starting...')
for i in range(10000000):
    y=random.randint(0, 100000)
    x.append(str(y))
x.sort()
print('ended...')
