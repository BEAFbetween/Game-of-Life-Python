import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

from main import DEAD, LIVE

def init_array(n, vals):
    return np.random.choice(vals, n*n, p=[0.2,0.8]).reshape(n, n)

def check_cell(array, i, j, n, newGrid):
    total = array[(i-1)%n,(j-1)%n] + array[(i-1)%n, j] + array[(i-1)%n, (j+1)%n] + array[i, (j+1)%n] + array[(i+1)%n, (j+1)%n] + array[(i+1)%n, j] + array[(i+1)%n, (j-1)%n] + array[i, (j-1)%n]
    if array[i,j] == LIVE:
        if (total < 2) or (total > 3):
            newGrid[i,j] = DEAD
    else:
        if total == 3:
            newGrid[i,j] = LIVE