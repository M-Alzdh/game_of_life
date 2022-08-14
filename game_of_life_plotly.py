import numpy as np
import plotly.express as px
import plotly.graph_objs as go

## this is my own implementation of a Conway's game of life
## it calculates all states to be plotted first and then plots them

## importing inital states from 'ready_input_csv
with open('ready_input_csv/acorn.csv') as file_name:
    input = np.loadtxt(file_name, delimiter=',')

## generating a random inital state
x = np.random.choice(2, (50, 50), p = [0.8, 0.2])

#set the number of generations
n_generations = 23

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
state_arrays = game_of_life(x, n_generations)

fig = go.Figure(
    data=[go.Heatmap(z=state_arrays[0])],
    layout=go.Layout(
        title="Frame 0",
        title_x=0.5,
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None]),
                    dict(label="Pause",
                         method="animate",
                         args=[None,
                               {"frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                                "transition": {"duration": 0}}],
                         )])]
    ),
    frames=[go.Frame(data=[go.Heatmap(z=state_arrays[i])],
                     layout=go.Layout(title_text=f"Frame {i}")) 
            for i in range(1, n_generations)]
)

fig.update_layout(showlegend=False)

fig.update_traces(showlegend=False)

fig.show()
