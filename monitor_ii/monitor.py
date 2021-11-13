"""
Monitors cpu load and prints to screen every 5 seconds
"""

import psutil
from time import sleep


def get_cpu_load():
    interval = 0
    loop = True

    while loop:
        print("CPU Load At:", psutil.cpu_percent(), "%")
        sleep(5)
        interval += 1
        if interval < 12:
            loop = True
        else:
            loop = False


if __name__ == "__main__":
    get_cpu_load()
