import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

def init_array(n, vals):
    return np.random.choice(vals, n*n, p=[0.2,0.8]).reshape(n, n)