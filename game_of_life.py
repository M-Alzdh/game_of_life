import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## this is my own implementation of a Conway's game of life
## it calculates all states to be plotted first and then plots them

## importing inital states from 'ready_input_csv
with open(r'game_of_life\ready_input_csv\acorn.csv') as file_name:
    input = np.loadtxt(file_name, delimiter=',')


## generating a random inital state
x = np.random.choice(2, (10, 10), p = [0.8, 0.2])
padded = np.pad(input, ((100, 100), (100, 100)), 'constant', constant_values = (0, 0) )
#set the number of generations
n_generations = 500

def game_of_life(x, generations = 10):
    imagelist = []
    first_step = x
    imagelist.append(first_step)
    shape = np.shape(x)
    num_neighbor = 1
    for x in range(generations):
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
        imagelist.append(next_step)
    return imagelist

## use "input" for imported initial state
state_arrays = game_of_life(padded, n_generations)

fig = plt.figure()
plot = plt.imshow(state_arrays[0], cmap='binary')

def update_plot(j):
    plot.set_array(state_arrays[j])
    return [plot]

ani = animation.FuncAnimation(fig, update_plot, frames=range(n_generations), interval = 50, blit = True)
plt.show()



