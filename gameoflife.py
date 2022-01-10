import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

from main import DEAD, LIVE

def init_array(n, vals):
    return np.random.choice(vals, n*n, p=[0.2,0.8]).reshape(n, n) # creates a square array of size n with probabilities p associated with either LIVE or DEAD

def update(array, i, j, n, newGrid): # totaling the number of LIVE cells neighbouring the chosen cell
    total = array[(i-1)%n,(j-1)%n] + array[(i-1)%n, j] + array[(i-1)%n, (j+1)%n] + array[i, (j+1)%n] + array[(i+1)%n, (j+1)%n] + array[(i+1)%n, j] + array[(i+1)%n, (j-1)%n] + array[i, (j-1)%n]
    if array[i,j] == LIVE: # applying Conway's rules
        if (total < 2) or (total > 3):
            newGrid[i,j] = DEAD
    else:
        if total == 3:
            newGrid[i,j] = LIVE
    
    img