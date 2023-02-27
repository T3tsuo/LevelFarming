from random import random


def leave_building():
    # 1.8 seconds to 1.9 seconds to leave building
    return random() * 0.1 + 1.8


def input_break():
    # break for hoping on bike from 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1


def inside_cave():
    # waits inside of cave for 1.5 second to 2 seconds
    return random() * 0.5 + 1.5


def below_cave():
    # 0.675 to 0.725
    return random() * 0.05 + 0.675


def into_cave():
    # 0.1 to 0.2 seconds
    return random() * 0.1 + 0.1


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
    return random() * 0.25 + 0.25
