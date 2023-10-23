import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random




run_dice = lambda : random.randint(1,6) == random.randint(1,6)

iter_num = 10000
iters = list(range(1,iter_num+1))
gains = []
roll_num = 1000
for i in iters:
    gain = 0
    for j in range(roll_num):
        if run_dice():
            gain = gain + 4
        else:
            gain -= 1
    
    gains.append(gain)
    
plt.plot(iters,gains)
    