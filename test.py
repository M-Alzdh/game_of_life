from operator import concat
import numpy as np
import matplotlib.pyplot as plt

with open('Conway.csv') as file_name:
    cway = np.loadtxt(file_name, delimiter=',')

print(cway)

x = np.zeros((10, 10))
x[1:4, 4] = 1
x[3, 3] = 1
x[2, 2] = 1


def game_of_life(x, generations = 100):
    
    first_step = x
    shape = np.shape(x)
    num_neighbor = 1
    plt.imshow(x, cmap='binary')
    plt.show()
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
        file_path = 'image_' + str(x) + '.png'
        print(file_name)
        first_step = next_step
        plt.imshow(first_step, cmap='binary')
        plt.savefig(file_path)
        
game_of_life(x)
