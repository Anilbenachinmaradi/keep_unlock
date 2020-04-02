import pyautogui as mouse
import time

size=mouse.size()

while True:
    sample=mouse.position()
    time.sleep(60)                          #If mouse is not moved for 60 seconds, program moves it for you..
    if sample==mouse.position():
        mouse.moveTo(size[0]/1.5,size[1]/2,duration = 1)
        mouse.moveTo(size[0]/3,size[1]/2,duration = 1)
