import numpy as np
import matplotlib.pyplot as plt
import random as rnd
# if 2 or more cells are alive the cell will remain alive/come to life

field1 = np.random.choice(2, size = (10, 10), p = [0.8, 0.2] )

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
        if np.sum(selection) > 2:
            field2[i, j] = 1
        

fig = plt.figure()
ax = fig.add_subplot(211)

plt.imshow(field1, cmap='binary')
ax = fig.add_subplot(221)

plt.imshow(field2, cmap='binary')
plt.show()


