import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import gameoflife

LIVE = 1
DEAD = 0
vals = [LIVE,DEAD]
init = gameoflife.init_array(6, vals) # create initial conditions in an array
newGrid = init.copy() # create a copy of that array that will become the grid after one time interval

fig, ax = plt.subplots()
img = plt.imshow(init, interpolation='nearest')

plt.show()