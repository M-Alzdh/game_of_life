import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open('ready_input_csv/acorn.csv') as file_name:
    input = np.loadtxt(file_name, delimiter=',')


x = np.random.choice(2, (100, 100), p = [0.8, 0.2])


def game_of_life(x, generations = 100):
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


y = game_of_life(input, 100)

fig = plt.figure()
im = plt.imshow(y[0], cmap='binary')

def update(j):
    im.set_array(y[j])
    return [im]

ani = animation.FuncAnimation(fig, update, frames=range(100), interval = 500, blit = True)
plt.show()

"""
hmpf = np.ones([4,4])
hmpf[2][1] = 0
imagelist = [ hmpf*i*255./19. for i in range(20) ]
print(imagelist)



fig = plt.figure() # make figure

# make axesimage object
# the vmin and vmax here are very important to get the color map correct
im = plt.imshow(imagelist[0], cmap=plt.get_cmap('jet'), vmin=0, vmax=255)

# function to update figure
def updatefig(j):
    # set the data in the axesimage object
    im.set_array(imagelist[j])
    # return the artists set
    return [im]
# kick off the animation
ani = animation.FuncAnimation(fig, updatefig, frames=range(20), 
                              interval=50, blit=True)
plt.show()
"""