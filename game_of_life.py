import numpy as np
import matplotlib.pyplot as plt
import random as rnd
# if 2 or more cells are alive the cell will remain alive/come to life

field1 = np.zeros((10, 10), np.int8)

field1[3:5, 1] = 1

shape = np.shape(field1)
field2 = np.zeros(shape = shape)

num_neighbor = 1

for i in range(shape[0]):
    for j in range(shape[1]):

        indx = [i, j]
        
        left = max(0, indx[0]-num_neighbor)
        right = max(0, indx[0]+num_neighbor+1)

        bottom = max(0,indx[1]-num_neighbor)
        top = max(0,indx[1]+num_neighbor+1)

        selection = field1[left:right, bottom:top]

        if np.sum(selection) >= 2:
            field2[i, j] = 1

print(field1, "\n", field2)

plt.imshow(field1)
plt.show()

plt.imshow(field2)
plt.show()


