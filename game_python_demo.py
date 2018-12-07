import numpy as np



universe = np.zeros((10, 10))
if universe[x, y] and not 2 <= num_neighbours <= 3:
    new_universe[x, y] = 0
elif num_neighbours == 3:
    new_universe[x, y] = 1


beacon = [[1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon



