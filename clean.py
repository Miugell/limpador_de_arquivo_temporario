import pyautogui
import time 

pyautogui.PAUSE = 1
pyautogui.hotkey('win', 'r')
pyautogui.write('temp')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.keyDown('shift')
pyautogui.press('delete')
pyautogui.keyUp('shift')
pyautogui.press('enter')
pyautogui.click(x=492, y=309)
pyautogui.click(x=726, y=336)
pyautogui.click()
pyautogui.hotkey('alt', 'f4')


pyautogui.hotkey('win', 'r')
pyautogui.write('%temp%')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.keyDown('shift')
pyautogui.press('delete')
pyautogui.keyUp('shift')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=492, y=309)
pyautogui.click(x=726, y=336)
pyautogui.click()
pyautogui.hotkey('alt', 'f4')   
