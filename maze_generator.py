import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint as rnd

def maze(width=81, height=51, complexity=.5, density =.5):
 
 h1 = (height//2)*2+1
 w1 = (width//2)*2+1
 grid = np.array([[0]*w1]*h1)

 # Adjust complexity and density relative to maze size
 complexity = int(complexity*(5*(h1+w1)))
 
 #density = int(density*(shape[0]//2*shape[1]//2))
 density = int(density*(h1//2*w1))
 
 # Make isles
 for _ in range(density):
    x, y = rnd(0,w1//2)*2, rnd(0,h1//2)*2
 
 grid[y,x] = 1
 
 for _ in range(complexity):
    neighbours = []
    if x > 1: neighbours.append( (y,x-2) )
    if x < w1-2: neighbours.append( (y,x+2) )
    if y > 1: neighbours.append( (y-2,x) )
    if y < h1-2: neighbours.append( (y+2,x) )
    if len(neighbours):
        y_,x_ = neighbours[rnd(0,len(neighbours)-1)]
    if grid[y_,x_] == 0:
        grid[y_,x_] = 1
    grid[y_+(y-y_)//2,x_+(x-x_)//2] = 1
    x, y = x_, y_
 
 #Make walls
 grid[0,:] = grid[-1,:] = 1
 grid[:,0] = grid[:,-1] = 1
 
 #Make doors
 grid[0,1]=0
 grid[h1-1,w1-2]=0
 
 return grid

import sys
np.set_printoptions(threshold=sys.maxsize)
maze = maze(100, 100, 100).tolist()
print(maze)
