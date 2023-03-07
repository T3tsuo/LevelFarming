import time
import pydirectinput
import pyautogui
import requests
from PIL import Image

import random_breaks


battle_done = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/LevelFarming/main/location/battle_done.png", stream=True).raw)

inside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/LevelFarming/main/location/inside_building.png", stream=True).raw)

tranquill = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/LevelFarming/main/battle_logs/tranquill.png", stream=True).raw)


def heal_up():
    at_nurse = False
    # we are not at nurse yet
    while at_nurse is False:
        # once we are at the nurse
        if pyautogui.locateOnScreen(inside_building, confidence=0.8) is not None:
            # then set flag to true, so we can talk to the nurse
            at_nurse = True
            print("At Nurse")
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
    # press teleport
    pydirectinput.press('5')
    print("Teleport")
    time.sleep(random_breaks.paying_attention_break())
    time.sleep(random_breaks.to_nurse())


def which_to_attack():
    print("SELECT #2")
    # select the second pokemon
    pydirectinput.press("z")
    time.sleep(random_breaks.paying_attention_break())


def kill_all():
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
            if pyautogui.locateOnScreen(battle_done, confidence=0.8) is not None:
                # then they are dead
                dead = True
                break


def run_away():
    pydirectinput.press('right')
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press('down')
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press('z')
    print('Run away')
    time.sleep(random_breaks.paying_attention_break())
    time.sleep(random_breaks.run_away_break())


def in_battle():
    while True:
        if pyautogui.locateOnScreen(tranquill, confidence=0.8) is not None:
            print("Run Away")
            return run_away()
        else:
            return kill_all()


def run(x):
    for i in range(x):
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