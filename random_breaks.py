from random import random


def leave_building():
    # 1.8 seconds to 1.9 seconds to leave building
    return random() * 0.1 + 1.8
