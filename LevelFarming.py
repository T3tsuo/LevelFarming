import os
import time

import fight
import heal_return

# this program xp levels pokemon

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"


def run():
    # else then ask for amount of times user can use sweet scent before going to pokecenter
    x = int(input("Number of times to use sweet scent: "))
    time.sleep(2)
    # loop forever
    while True:
        heal_return.run()
        fight.run(x)
