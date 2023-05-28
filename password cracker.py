import random
import string
import time
import keyboard
import pyautogui

def type_random_text():
    pyautogui.click()
    text = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    pyautogui.write(text)
    pyautogui.press('enter')

def repeat_function():
    while True:
        if keyboard.is_pressed('f9'):
            start_time = time.time()
            while not keyboard.is_pressed('f9'):
                if keyboard.is_pressed('f10'):
                    return
                type_random_text()
                time.sleep(max(0, 0.001 - (time.time() - start_time)))
                start_time = time.time()

repeat_function()