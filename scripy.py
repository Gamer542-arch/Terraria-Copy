import pyautogui as pag
import time
import os
import keyboard
# Pisanie tekstu
while True:
    by =+ 1
    nick = "Nick" # here your nickname
    text = "67, i have sub and like the live My username is {nick}"
    pag.write(text.format(nick=nick))
    pag.press("enter")
    pag.press("enter")
    time.sleep(3)
    if by == 2 or keyboard.is_pressed("q"):
        break