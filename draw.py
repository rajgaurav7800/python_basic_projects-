import pyautogui, time
time.sleep(1)
print('runing')
pyautogui.click()
d = 400
min = 2

while d > 0:
    pyautogui.dragRel(d, 0, duration=0.1)
    d -= min
    pyautogui.dragRel(0, d, duration=0.1)
    pyautogui.dragRel(-d, 0, duration=0.1)
    d -= min
    pyautogui.dragRel(0, -d, duration=0.2)

print('finish')