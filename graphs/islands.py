'''
Get the number of islands in the water using bfs technique of graphs
the islands are groups of 1's among the water of 0s
'''
from collections import deque

def numIslands(grid):
    #if there is no grid, there are no islands
    if not grid:
        return 0
    #the idea is to use bfs to group together all adjacent 1's
    visited = set()
    islands = 0
    rows, cols = len(grid), len(grid[0])

    #the bfs function
    def bfs(r, c):
        q = deque()
        q.append((r, c)) #add this to the queue
        visited.add((r, c))
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            row, col = q.popleft()
            for dr, dc in dirs:
                r, c = row+dr, col+dc
                #make sure that this r, c are in bounds
                if 0<=r<rows and 0<=c<cols and grid[r][c] == "1" and (r, c) not in visited:
                    #clumping condition, mark them as visited
                    q.append((r, c))
                    visited.add((r, c))
        #this function will not visit the already visited nodes, go through all the neighbours of 1, and
        #clump them together in the queue, and when popping them marks them as visited

    #iterate through all elements in the grid
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and grid[r][c] == "1":
                islands += 1 #increment islands by 1, run bfs to clump adjacent 1's together
                bfs(r, c)
    return islands

grid1 = [
    ["1", "0", "0", "0", "1", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "0", "0", "0", "0", "0", "1"],
    ["0", "1", "0", "0", "0", "1", "0", "0", "1", "0"],
    ["0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0", "0", "0", "0", "0", "0"],
    ["1", "0", "0", "0", "0", "1", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "1", "0"],
    ["0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1", "0", "0", "0", "0", "0"]
]

print("\n grid-1", numIslands(grid1))

def maxAreaOfIsland(grid):
    #intialize a set that tracks the nodes that are visited, row, and col length
    ROW, COL = len(grid), len(grid[0])
    area_max = 0
    if not grid:
        return area_max
    def bfs(r, c, area_max):
        curr_area = 0
        q = deque()
        q.append((r, c))
        grid[r][c] = 0
        curr_area += 1
        while q:
            #while the queue is non empty, add the neighbours of this node that are 1's and increase
            #the area
            r, c = q.popleft()
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in dirs:
                #make sure that we don't go out of bounds
                if 0 <= r+x < ROW and 0 <= c+y < COL and grid[r+x][c+y] == 1:
                    q.append((r+x, c+y))
                    grid[r+x][c+y] = 0
                    curr_area += 1
        return curr_area


    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1:
                #perform BFS only the unvisited 1's which could lead us to new islands
                area_max = max(bfs(r, c, area_max), area_max)
    return area_max

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))