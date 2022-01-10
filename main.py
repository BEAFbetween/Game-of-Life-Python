import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

LIVE = 1
DEAD = 0
vals = [LIVE,DEAD]
n = 100

def init_array(n):
    return np.random.choice(vals, n*n, p=[0.2,0.8]).reshape(n, n) # creates a square array of size n with probabilities p associated with either LIVE or DEAD

def update(frameNum, img, array, n): # totaling the number of LIVE cells neighbouring the chosen cell
    for i in range(n): # iterating over the whole grid
        for j in range(n):
            total = array[(i-1)%n,(j-1)%n] + array[(i-1)%n, j] + array[(i-1)%n, (j+1)%n] + array[i, (j+1)%n] + array[(i+1)%n, (j+1)%n] + array[(i+1)%n, j] + array[(i+1)%n, (j-1)%n] + array[i, (j-1)%n]
            if array[i,j] == LIVE: # applying Conway's rules
                if (total < 2) or (total > 3):
                    newGrid[i,j] = DEAD
            else:
                if total == 3:
                    newGrid[i,j] = LIVE
    img.set_data(newGrid)
    array[:] = newGrid[:]
    return img

def glider(i, j, array): # add glider with top left cell i,j
    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    array[i:i+3, j:j+3] = glider
    

init = init_array(n) # create initial conditions in an array
# init = np.zeros(n*n).reshape(n,n) # checks to see if it is working
# glider(3, 3, init)
newGrid = init.copy() # create a copy of that array that will become the grid after one time interval

fig, ax = plt.subplots()
img = plt.imshow(init, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, init, n), frames = 10)

plt.show()