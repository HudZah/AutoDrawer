import time
import sys
import os

cwd = os.getcwd()

from mouseAutomater import ImageController
from mouseAutomater import MouseAutomater

lsleep = 0.002
rsleep = 0.025
print("Created by HudZah\n\n\n")

imageName = ImageController.getImage()
handler = ImageController(imageName)
resizeValue = int(input("Output pixel size (for square image): "))
offset = int(input("Scale for image (1 for one to one): "))
resizeValue = resizeValue / offset
handler.convertToBW()
handler.resize(resizeValue)

returnKey = None
while returnKey == None:
    MouseAutomater.openPaint()
    print("Warning: There is no fail-safe other than pulling your mouse to the upper left corner, in case anything goes wrong once you start this program please abort using Ctrl + Alt + Delete \n\n\n")
    print("Enter to start 3 second countdown, N to abort, pull to left hand corner to abort once the program starts")
    print("Please position your cursor on a canvas on either Paint, Photoshop or any other design software as soon as you start running this. Make sure there is optimal space to completely draw the image.")
    returnKey = input()
    returnKey = returnKey.lower()
    if returnKey == "n":
        exit()
    
time.sleep(3)
array = handler.newImageArray()
MouseAutomater.imageToLines(array, offset, rsleep, lsleep)
repeat = "y"
while repeat == "y":
    repeat = input("Type 'y' to repeat, or enter to exit")
    repeat = repeat.lower()
    if repeat == "y":
        time.sleep(3)
        MouseAutomater.imageToLines(array, offset, rsleep, lsleep)
    else:
        exit()

