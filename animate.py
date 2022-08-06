import cmath
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.zeros((10, 10))
x[1:4, 4] = 1
x[3, 3] = 1
x[2, 2] = 1

first_step = x
image = None
next_step = None


def generator(generation):
    global image, first_step
    next_step = np.zeros_like(first_step)
    shape = np.shape(first_step)
    num_neighbor = 1
    if generation < 5:
        next_step = first_step
    else:
        next_step = np.zeros(shape = shape)
        for i in range(shape[0]):
            for j in range(shape[1]):

                indx = [i, j]
                
                left = max(0, indx[0]-num_neighbor)
                right = max(0, indx[0]+num_neighbor+1)

                bottom = max(0,indx[1]-num_neighbor)
                top = max(0,indx[1]+num_neighbor+1)

                selection = first_step[left:right, bottom:top]
                sum = (np.sum(selection))- first_step[i, j]
                                
                if first_step[i, j] == 1 and (sum == 2 or sum == 3):
                    next_step[i, j] = 1
                elif first_step[i, j] == 0 and sum == 3: 
                    next_step[i, j] = 1
                else:
                    next_step[i, j] = 0

        first_step = next_step
    image.set_data(next_step)
        #plt.imshow(first_step, cmap='binary')
        #plt.show()
    return image,


def game_of_life(x):
    global image, first_step
    fig, ax = plt.subplots(figsize = (8, 8))
    image = ax.imshow()
    ani = animation.FuncAnimation(fig, frames=100, func=generator, interval = 100)
    plt.show()
    return ani
"""
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

y = conway_step(4)
print(y)

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
    ani.save('testconway.gif')
    plt.show()
    return ani

conway(size=100)
"""