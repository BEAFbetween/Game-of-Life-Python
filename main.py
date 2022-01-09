import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
import gameoflife

LIVE = 1
DEAD = 0
vals = [LIVE,DEAD]
init = gameoflife.init_array(6, vals)