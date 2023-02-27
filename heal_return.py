import time
import requests
import pydirectinput
import pyautogui
from PIL import Image

import random_breaks

outside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/outside_building.png", stream=True).raw)

inside_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/inside_cave.png", stream=True).raw)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    print("Left building")
    # while cannot find outside, keep on waiting
    is_outside = False
    while is_outside is False:
        # if image recognition detects that we left the building
        if pyautogui.locateOnScreen(outside_building, confidence=0.8) is not None:
            # then we are outside
            is_outside = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)


def go_to_cave():
    # hop on bike
    pydirectinput.press("1")
    print("Bicycle")
    time.sleep(random_breaks.input_break())
    # go right
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.below_cave())
    pydirectinput.keyUp("right")
    time.sleep(random_breaks.input_break())
    # go into cave
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.into_cave())
    pydirectinput.keyUp("up")
    # break 1.5 - 2 seconds
    time.sleep(random_breaks.inside_cave())
    in_cave = False
    while in_cave is False:
        # use image detection to make sure we are inside the cave
        if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
            in_cave = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)
    print("Inside of Cave")
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())
