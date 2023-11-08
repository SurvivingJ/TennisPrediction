import random
from time import sleep

def bot_sleep(min_time = 1, max_time = 10, force = False):
    activate = random.randint(1, 2)
    if activate == 1 or force is True:
        sleep_time = random.randint(min_time, max_time)
    else:
        sleep_time = 0

    sleep(sleep_time)
    return True