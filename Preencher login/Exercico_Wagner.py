from time import sleep
import pyautogui
pyautogui.press('Win')
sleep(2)
pyautogui.write('Edge', interval=0.4)
pyautogui.press('enter')
sleep(2)

link_login = "http://127.0.0.1:5500/index.html"
pyautogui.write(link_login, interval=0.2)
sleep(1)
pyautogui.press("enter")
sleep(1)
pyautogui.press("tab")
pyautogui.write("admin", interval=0.2)
sleep(1)
pyautogui.press("tab")
pyautogui.write("admin", interval=0.2)
sleep(1)
pyautogui.press("tab")
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.press("enter")


