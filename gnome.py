import pyautogui
import time
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.press('win')
pyautogui.typewrite('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.typewrite('https://www.youtube.com/watch?v=6n3pFFPSlW4')
pyautogui.press('enter')
