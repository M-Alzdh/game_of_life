import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## this is my own implementation of a Conway's game of life
## it calculates all states to be plotted first and then plots them

## importing inital states from 'ready_input_csv
with open(r'game_of_life\ready_input_csv\worms.csv') as file_name:
    input = np.loadtxt(file_name, delimiter=',')

filter_array = np.array(([0.8, -0.85, 0.8], [-0.85, -0.2, -0.85], [0.8, -0.85, 0.8]))
filter_slime = np.array(([0.8, -0.85, 0.8], [-0.85, -0.2, -0.85], [0.8, -0.85, 0.8]))
filter_waves = np.array(([0.565, -0.716, 0.565], [-0.716, 0.627, -0.716], [0.565, -0.716, 0.565]))

def activation_func(x):
    return -1/(0.89*(x**2)+1)+1

def waves_activation(x):
    return abs(1.2*x)

def clip(x):
    if x>1:
        return 1
    if x<-1:
        return -1
    return x

## generating a random inital state
x = np.random.choice(2, (200, 200), p = [0.8, 0.2])
init_worm = np.random.choice([0, 1], (50, 50), p = (0.8, 0.2))
padded = np.pad(x, ((1, 1), (1, 1)), 'constant', constant_values = (0, 0) )
#set the number of generations
n_generations = 1000

def game_of_life(x, generations = 10):
    imagelist = []
    first_step = x
    imagelist.append(first_step)
    shape = np.shape(x)
    num_neighbor = 1
    for x in range(generations):
        next_step = np.zeros(shape = shape)
        for i in range(1,shape[0]-1):
            for j in range(1, shape[1]-1):

                indx = [i, j]
                
                left = max(0, indx[0]-num_neighbor)
                right = max(0, indx[0]+num_neighbor+1)

                bottom = max(0,indx[1]-num_neighbor)
                top = max(0,indx[1]+num_neighbor+1)

                selection = first_step[left:right, bottom:top]
                filtered = selection*filter_waves
                sum = np.sum(filtered)#- first_step[i, j]
                activated = clip(waves_activation(sum))
                                
                next_step[i, j] = activated
        first_step = next_step
        imagelist.append(next_step)
    return imagelist

## use "input" for imported initial state
state_arrays = game_of_life(padded, n_generations)



fig = plt.figure()
plot = plt.imshow(state_arrays[0], cmap='copper')
ax = plt.gca()

ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

def update_plot(j):
    plot.set_array(state_arrays[j])
    return [plot]

ani = animation.FuncAnimation(fig, update_plot, frames=range(n_generations), interval = 100, blit = True)
plt.show()


f = r"c://Users/Haji/Desktop/animation3.gif" 
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
