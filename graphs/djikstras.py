'''
Shortest path graph algorithm - It is used to find the shortest path from node to all the other nodes in the graph.
Set the initial node distance to 0 and all the other nodes as tentative - inf
Once we visit a node and compute the distance, we mark it visited and do not visit it again
The next node is selected as the unvisited node with the smallest tentative distance.
This is a greedy algorithm because it selects the shortest distance at each step, the time complexity is O(E + V)(log V) if we use a heap
This algorithm cannot work for unconnected components or for negative weights
'''
from collections import defaultdict
import heapq as hq
def networkDelayTime(times, n, k):
    adj = defaultdict(list)
    visited = set() #to track the nodes we visited and to help in the break case
    for s, d, time in times:
        adj[s].append([time, d])
    #initialize the min_heap with the starting node which is k in the problem
        #min_heap contains [distance, node]
    t = 0
    min_heap = [[0, k]]
    while min_heap:
        time, node = hq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        t = time
        #now bfs-ly add the neighbors of node to heap
        for next_time, next_node in adj[node]:
            if next_node not in visited:
                hq.heappush(min_heap, [next_time + time, next_node]) #we add the time it took to reach the previous node, plus the time
                                                                        #to reach the next node
    return t if len(visited) == n else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n, k = 4, 2
print("\n the minimum time to reach all points is : ", networkDelayTime(times, n, k))


def minimumEffortPath(heights) -> int:
        #to return the path with abs min diff in heights btw consecutive cells
        ROW, COL = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]] #diff, r, c
        visited = set() #to mark the nodes as visited
        #use a BFS plus heap - Dijkstra's alg
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while min_heap:
            diff, r, c = hq.heappop(min_heap)
            if (r,c) in visited:
                continue #skip this iteration as this node is already visited
            visited.add((r, c))
            #break case when we reach the bottom right cell
            if (r, c) == (ROW - 1, COL - 1):
                return diff
            #go through every neighbor of this certain cell
            for x, y in dirs:
                if 0 <= r+x < ROW and 0 <= c+y < COL and (r+x, c+y) not in visited:
                    #the cell is in bound, add the neighbor to the heap
                    #the diff is the height diff btw two cells
                    h_diff = max(diff, abs(heights[r+x][c+y] - heights[r][c]))
                    hq.heappush(min_heap, [h_diff, r+x, c+y])
                    #the min_heap only ever pushes the min_height diff, so even it goes greedily
                    #to the shortest diff, it will stop eventually when it hits a big h_diff in that path
heights = [[1,2,3],[3,8,4],[5,3,5]]
print("\n the min effort to reach the bot right cell is :", minimumEffortPath(heights))