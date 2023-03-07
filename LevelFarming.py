import sys
import os
import time

# import fight
import heal_return

# this program grabs items and then fly's to go restore pokemon pp

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

try:
    # try to grab input from command line for amount of sweet scent
    x = int(sys.argv[1])
except IndexError:
    # else then ask for amount of times user can use sweet scent before going to pokecenter
    x = int(input("Number of times to use sweet scent: "))
time.sleep(2)
# loop forever
while True:
    heal_return.run()
    # fight.run(x)
