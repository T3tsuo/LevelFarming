import time
import requests
import pydirectinput
import pyautogui
from PIL import Image

import random_breaks

outside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/LevelFarming/main/location/outside_building.png", stream=True).raw)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    # while cannot find outside, keep on waiting
    is_outside = False
    while is_outside is False:
        # if image recognition detects that we left the building
        if pyautogui.locateOnScreen(outside_building, confidence=0.8) is not None:
            # then we are outside
            is_outside = True
            print("Left building")
            time.sleep(0.5)
        else:
            time.sleep(0.5)


def go_to_grass():
    # hop on bike
    pydirectinput.press("1")
    print("Bicycle")
    time.sleep(random_breaks.input_break())
    # go left
    pydirectinput.keyDown("left")
    time.sleep(4)
    pydirectinput.keyUp("left")
    print("There")
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())

def run():
    leave_building()
    go_to_grass()
