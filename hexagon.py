import pyautogui, time
time.sleep(1)
print('runing')
pyautogui.click()
d = 10
ti = 10000
for q in range(10):
    for i in range(ti):
        pyautogui.dragRel(+d, 0)  # --->
    for i in range(ti):
        pyautogui.dragRel(d, 0)  # \
        pyautogui.dragRel(0, d)
    for i in range(ti):
        pyautogui.dragRel(0, d)
    for i in range(ti):
        pyautogui.dragRel(0, d)  # /
        pyautogui.dragRel(-d, 0)
    for i in range(ti):
        pyautogui.dragRel(-d, 0)  # <---
    for i in range(ti):
        pyautogui.dragRel(-d, 0)  # \
        pyautogui.dragRel(0, -d)
    for i in range(ti):
        pyautogui.dragRel(0, -d)
    for i in range(ti):
        pyautogui.dragRel(0, -d)  # /
        pyautogui.dragRel(d, 0)

min = 20

print('finish')

# for i in range(ti):
#     pyautogui.dragRel(d, 0)     #\
#     pyautogui.dragRel(0, d)