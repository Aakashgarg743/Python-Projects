from numpy.lib.type_check import imag
import pyautogui
from PIL import Image, ImageGrab
import time
from numpy import asarray, histogram

# pyautogui.keyDown("a")
# pyautogui.keyDown("a")
# pyautogui.keyDown("k")
# pyautogui.keyDown("a")
# pyautogui.keyDown("s")
# pyautogui.keyDown("h")

# Take Screnshot
# image = ImageGrab.grab().convert('L')
# image.show()

# DINO GAME

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(695, 720):
        for j in range(300, 320):
            data[i, j] < 100
            return True
    return False

if __name__=='__main__':
    print("The Game is going to start in 5 seconds...")
    time.sleep(5)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        # print(asarray(image))
        if isCollide(data):
            hit("up")
        else:
            hit("down")
    # time.sleep(2)
    # image = ImageGrab.grab().convert('L')
    # data = image.load()
    # for i in range(680, 720):
    #     for j in range(310, 330):
    #         data[i, j] = 0

    # image.show()