def get_land_neighbors(i, j, grid):
 """ returns list of neighbor's positions """
 output = []
 for ni, nj in [(i+1, j),(i-1, j),(i, j+1),(i, j-1)]:
   if(0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj]):
     output.append((ni, nj))
 return output

def islands_plot(grid):
 num_islands = 0
 seen = set()
 for i in range(len(grid)):
   for j in range(len(grid[0])):
     if grid[i][j] and (i,j) not in seen:
       seen.add((i, j))
       num_islands += 1
       neighbors = get_land_neighbors(i, j, grid)
       while neighbors:
         current = neighbors.pop()
         if current in seen:
           continue
         else:
           neighbors.extend(get_land_neighbors(current[0], current[1], grid))
           seen.add(current)
 return num_islands


print(islands_plot([[1,1,1,0],
                    [0,1,0,1],
                    [1,0,0,1]]))