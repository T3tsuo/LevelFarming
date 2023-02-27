import time
import pydirectinput
import pyautogui
import requests
from PIL import Image

import random_breaks


inside_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/inside_cave.png", stream=True).raw)

victory_road = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/victory_road.png", stream=True).raw)

inside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/XPLevel/main/location/inside_building.png", stream=True).raw)


def heal_up():
    at_nurse = False
    # we are not at nurse yet
    while at_nurse is False:
        # once we are at the nurse
        if pyautogui.locateOnScreen(inside_building, confidence=0.8) is not None:
            # then set flag to true, so we can talk to the nurse
            at_nurse = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)

    # talk through dialogue
    print("Talking to Nurse")
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.heal_up_break())
    pydirectinput.keyUp("z")
    print("Healing Done")
    # break
    time.sleep(random_breaks.input_break())


def teleport_away():
    # use dig
    pydirectinput.press("6")
    print("Dig")
    time.sleep(random_breaks.paying_attention_break())
    left = False
    while left is False:
        # once left the cave
        if pyautogui.locateOnScreen(victory_road, confidence=0.8) is not None:
            # wait for screen to change
            time.sleep(random_breaks.paying_attention_break())
            # press teleport
            pydirectinput.press('5')
            print("Teleport")
            left = True
            time.sleep(random_breaks.paying_attention_break())
            print("At Nurse")
            time.sleep(random_breaks.to_nurse())


def which_to_attack():
    print("SELECT #2")
    # select the second pokemon
    pydirectinput.press("z")
    time.sleep(random_breaks.paying_attention_break())


def in_battle():
    dead = False
    # break from 1.5 - 2 seconds
    time.sleep(random_breaks.inside_cave())
    while not dead:
        # press fight
        pydirectinput.press('z')
        print("Fight")
        time.sleep(random_breaks.paying_attention_break())
        # go to second move
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # press surf/earthquake (second move)
        pydirectinput.press('z')
        print("Earthquake/Surf")
        time.sleep(random_breaks.paying_attention_break())
        # select and attack the second pokemon
        which_to_attack()
        # wait for entire attack break while checking if thief took an item
        seconds = random_breaks.attack_break()
        end_time = time.time() + seconds
        while time.time() < end_time:
            # if battle is done
            if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
                # then they are dead
                dead = True
                break


def run(x):
    for i in range(x):
        # wait for program to switch to game window
        time.sleep(random_breaks.run_away_break())
        # use sweet scent
        pydirectinput.press('4')
        print("Sweet Scent")
        time.sleep(random_breaks.starting_battle_break())
        # use fight them to gain xp
        in_battle()
    # when all of sweet scent is used then leave to pokecenter
    teleport_away()
    # then heal up
    heal_up()