import time
import sys
import os

cwd = os.getcwd()

from mouseAutomater import ImageController
from mouseAutomater import MouseAutomater

lsleep = 0.002
rsleep = 0.025
print("Created by HudZah\n\n\n")

def getInput():
    imageName = ImageController.getImage()
    resizeValue = int(input("Enter the output pixel size (for a square image): "))
    offset = int(input("Enter the scale for the image (1 for one to one): "))
    resizeValue = resizeValue / offset
    return imageName, resizeValue, offset

def processImage(imageName, resizeValue):
    handler = ImageController(imageName)
    handler.convertToBW()
    handler.resize(resizeValue)
    return handler

def drawImage(handler, offset):
    array = handler.newImageArray()
    MouseAutomater.imageToLines(array, offset, lsleep, lsleep)

def main():
    imageName, resizeValue, offset = getInput()
    handler = processImage(imageName, resizeValue)
    drawImage(handler, offset)

main()
