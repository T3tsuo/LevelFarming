import time
import requests
import pydirectinput
import pyautogui
from PIL import Image

import random_breaks

outside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/outside_building.png", stream=True).raw)


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

time.sleep(2)
leave_building()
