import time
import socket
import pyautogui

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        time.sleep(60)
        s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        print("Sin conexión a internet")
        pyautogui.click(1191, 744)
        time.sleep(2)
        pyautogui.click(1120, 670)
        time.sleep(4)
        pyautogui.click(1120, 670)
        time.sleep(1)
        pyautogui.click(1126, 740)
        time.sleep(1)
        continue
    else:
        print("Con conexión a internet")
        internet = True
        s.close()
        time.sleep(20)
        continue

