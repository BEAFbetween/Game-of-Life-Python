import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

LIVE = 1
DEAD = 0
vals = [LIVE,DEAD]
n = 100

def init_array(n):
    return np.random.choice(vals, n*n, p=[0.2,0.8]).reshape(n, n)   # creates a square array of size n with probabilities p associated with either LIVE or DEAD

def update(frameNum, img, array, n):    # totaling the number of LIVE cells neighbouring the chosen cell
    for i in range(n):                  # iterating over the whole grid
        for j in range(n):
            total = array[(i-1)%n,(j-1)%n] + array[(i-1)%n, j] + array[(i-1)%n, (j+1)%n] + array[i, (j+1)%n] + array[(i+1)%n, (j+1)%n] + array[(i+1)%n, j] + array[(i+1)%n, (j-1)%n] + array[i, (j-1)%n]
            if array[i,j] == LIVE:      # applying Conway's rules
                if (total < 2) or (total > 3):
                    newGrid[i,j] = DEAD
            else:
                if total == 3:
                    newGrid[i,j] = LIVE
    img.set_data(newGrid)
    array[:] = newGrid[:]
    return img

def glider(i, j, array):            # add glider with top left cell i,j
    glider = np.array([[0, 0, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
    array[i:i+3, j:j+3] = glider    # positions glider at top left of the array

def pulsar(i, j, array):                # add pulsar with top left cell i,j
    pulsar = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                       [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                       [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                       [0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
                       [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    array[i:i+15, j:j+15] = pulsar  # positions pulsar at top left of array

def glider_gun(i, j, array):
    glider_gun = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                           [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                           [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    array[i:i+9, j:j+36] = glider_gun
    
print("Please choose from one of the following options:")
print("1. Random DEAD and ALIVE cells")
print("2. A pulsar")
print("3. A glider gun")
choice = input()

match choice:
    case '1':
        init = init_array(n)
    case '2':
        n = 19
        init = np.zeros(n*n).reshape(n,n)   # initialising the array so the pulsar is central and fits the screen
        pulsar(2, 2, init)
    case '3':
        init = np.zeros(n*n).reshape(n,n)
        glider_gun(3, 3, init)

#init = init_array(n)                # create initial conditions in an array
#init = np.zeros(n*n).reshape(n,n)   # creating a completely DEAD array
## glider(3, 3, init)
## pulsar(3, 3, init)
#glider_gun(3, 3, init)
newGrid = init.copy()               # create a copy of that array that will become the grid after one time interval

fig, ax = plt.subplots()
img = plt.imshow(init, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, init, n), frames = 10)

plt.show()