# https://en.wikipedia.org/wiki/Isochrone_map

import numpy as np
import matplotlib.pyplot as plt
                              

def check_around_position(x, y, energy):
  poss_moves = [[x, y+1, False],
                [x+1, y+1, True],
                [x+1, y, False],
                [x+1, y-1, True],
                [x, y-1, False],
                [x-1, y-1, True],
                [x-1, y, False],
                [x-1, y+1, True]] 
  for poss_move in poss_moves:
    x, y, diag = poss_move
    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]): # not on edge
      if grid[x][y][1] == 0: # not visited before
        cost =  grid[x][y][0]
        if diag:
          cost = np.sqrt(2 * (cost)**2)
        poss_energy = energy - cost
        if poss_energy >= 0:
          if (x, y) not in MOVES:
            MOVES[(x, y)] = poss_energy
          elif poss_energy > MOVES[(x, y)]:
            print ('Exchange: ', (x, y), MOVES[(x, y)], poss_energy)
            MOVES[(x,y)] = poss_energy



#Example 1

grid = [[[10, 0], [20, 0], [10, 0]],
        [[20, 0], [0, 0], [10, 0]],
        [[20, 0], [20, 0], [20, 0]]]

center=(1, 1)
total_energy=100

MOVES = {center: total_energy}
while MOVES:
  print (MOVES)
  max_move = max(MOVES, key=MOVES.get) 
  max_energy = MOVES.pop(max_move)
  grid[max_move[0]][max_move[1]][1] = max_energy
  check_around_position(max_move[0], max_move[1], max_energy)


plt.matshow([[x[1] for x in y] for y in grid])
plt.show()


#Example 2          
grid = [[[1, 0],  [1, 0], [1, 0], [1, 0], [1, 0]],
        [[1, 0], [60, 0], [50, 0], [40, 0], [1, 0]],
        [[1, 0], [70, 0], [0, 0], [30, 0], [1, 0]],
        [[1, 0],  [80, 0], [1, 0], [1, 0],  [1, 0]]]

center=(2, 2)
total_energy=100
MOVES = {center: total_energy}
while MOVES:
  print (MOVES)
  max_move = max(MOVES, key=MOVES.get)
  max_energy = MOVES.pop(max_move)
  grid[max_move[0]][max_move[1]][1] = max_energy
  check_around_position(max_move[0], max_move[1], max_energy)

plt.matshow([[x[1] for x in y] for y in grid])
plt.show()
          

#Example 3

grid_size = 10 
grid = [[[10,0] for _ in range(grid_size)] for _ in range(grid_size)]

center=(2, 2)
total_energy=100
MOVES = {center: total_energy}
while MOVES:
  print (MOVES)
  max_move = max(MOVES, key=MOVES.get)
  max_energy = MOVES.pop(max_move)
  grid[max_move[0]][max_move[1]][1] = max_energy
  check_around_position( max_move[0], max_move[1], max_energy)

plt.matshow([[x[1] for x in y] for y in grid])
plt.show()




#Example 4

grid_size = 300 
grid = [[[np.random.randint(1,10),0] for _ in range(grid_size)] for _ in range(grid_size)]

center=(round(grid_size/2), round(grid_size/2))
total_energy=250
MOVES = {center: total_energy}
while MOVES:
  max_move = max(MOVES, key=MOVES.get)
  max_energy = MOVES.pop(max_move)
  grid[max_move[0]][max_move[1]][1] = max_energy
  check_around_position( max_move[0], max_move[1], max_energy)

plt.matshow([[x[1] for x in y] for y in grid])
plt.show()






import pdb; pdb.set_trace()
