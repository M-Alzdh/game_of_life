import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.colors import ListedColormap
import numpy as np

## this code is copied from 
## https://stackoverflow.com/questions/70019538/simple-animation-for-conways-game-of-life-with-funcanimation
## it is more efficient sice it does not calculate all states of the system before plotting

grid, grid_size, img_plot = None, None, None

def initialize(size):
    grid = np.random.choice([0, 1], size * size, p=[0.8, 0.2]).reshape(size, size)
    return grid

def conway_step(frame):
    global grid, grid_size, img_plot
    if frame < 3:   # no movement for the first few steps
        new_grid = grid
    else:
        new_grid = np.zeros_like(grid)
        for x in range(grid_size):
            for y in range(grid_size):
                total = sum(
                    [grid[(x + i) % grid_size, (y + j) % grid_size] for i in range(-1, 2) for j in range(-1, 2)])
                if grid[x, y] == 1 and total - 1 in (2, 3):
                    new_grid[x, y] = 1
                elif grid[x, y] == 0 and total == 3:
                    new_grid[x, y] = 1
                else:
                    new_grid[x, y] = 0
        grid = new_grid
    img_plot.set_data(new_grid)
    return img_plot,

def conway(random=True, size=100):
    global grid, grid_size, img_plot
    grid_size = size
    grid = initialize(size)
    fig, ax = plt.subplots(figsize=(10, 10))
    img_plot = ax.imshow(grid, interpolation='nearest', cmap=ListedColormap(['darkturquoise', 'yellow']))
    ax.set_xticks([])
    ax.set_yticks([])
    ani = animation.FuncAnimation(fig, frames=100, func=conway_step, interval=100)
    plt.tight_layout()
    plt.show()
    return ani

conway(size=200)