from itertools import cycle, permutations, combinations, product
import sys
import time
import os

"""Traffic lighter in a terminal using itertools"""


lights = '* O O'.split()
positions = ['\n'.join(i) for i in list(permutations(lights))[1:-1]]
traffic_light = cycle(positions)
os.system("clear")
while True:
    sys.stdout.write(next(traffic_light))
    sys.stdout.flush()
    time.sleep(5)
    os.system("clear")
    sys.stdout.write(next(traffic_light))
    sys.stdout.flush()
    time.sleep(1)
    os.system("clear")

