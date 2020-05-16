import numpy as np
import pyautogui
import time
import os
from PIL import Image, ImageFilter, ImageOps

class MouseAutomater(object):

    pyautogui.PAUSE = 0.00
    pyautogui.FAILSAFE = True

    def openPaint():
        openPain = input("Would you like to open paint? (yes to continue) (Windows only)")
        if openPain == "yes":
            os.startfile("C:\WINDOWS\system32\mspaint.exe")

    @staticmethod
    def imageToLines(imageArray : np.array, offset: int, rsleep:int, lsleep:int) -> None:
        startPosX,startPosY = pyautogui.position()

        for row in imageArray:
            xoffset = 0
            isDrawing = False
            for value in row:
                if value == False: # Don't draw
                    if isDrawing == True:
                        xoffset += offset
                    else:
                        startLine = startPosX + xoffset
                        isDrawing = True
                        xoffset += offset
                if value == True:
                    if isDrawing == False:
                        xoffset += offset
                    else:
                        pyautogui.moveTo(startLine, startPosY)
                        pyautogui.dragTo(startPosX + xoffset, startPosY, duration=lsleep, button="left")
                        time.sleep(lsleep)
                        isDrawing = False
                        xoffset += offset
            if value == False:
                if isDrawing == True:
                    pyautogui.moveTo(startLine, startPosY)
                    pyautogui.dragTo(startPosX + xoffset, startPosY, duration=lsleep, button="left")
                    time.sleep(lsleep)
                    xoffset += offset
            startPosY += offset
            time.sleep(rsleep)


class ImageController(object):
    def __init__(self, image):
        self.image = Image.open(image)
    
    @staticmethod
    def getImage() -> str:
        path = input("Path to image: ")
        return path
    
    def convertToBW(self) -> None:
        self.image = self.image.convert(mode="1" , dither=None)

    def invertImage(self, image) -> None:
        self.image = ImageOps.invert(Image.open(image))

    def resize(self, resizeValue) -> None:
        horSize, verSize = self.image.size

        if horSize > verSize:
            conversion = horSize/ resizeValue
            self.image = self.image.resize((int(horSize/ conversion), int(verSize/ conversion)))
        else:
            conversion = verSize/ resizeValue
            self.image = self.image.resize((int(horSize/conversion), int(verSize/conversion)))
        
    def newImageArray(self) -> np.array:
        array = np.array(self.image)
        return array
