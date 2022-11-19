import pyautogui
import time
print("start in 20 seconds")
time.sleep(20)
print('start')
n=1
przycisk = 'txt'
while n<26:
	przycisk = str(n)+'.png'
	print("Searching for "+str(n))
	pyautogui.click(pyautogui.locateCenterOnScreen(przycisk))
	print("Found [?]")
	
	n=n+1
print('Done')