'''
Prim's algorithm is used to find the minimum spanning tree for a given graph of E edges, and V vertices.
The time complexity is ElogV
Start at any vertex in the graph and perform BFS on that, we maintain two data structures - a visit hash-set and a min-heap
The hash-set doesn't add the same vertex twice and prevents cycles
The min-heap tracks our frontier - add all possible edges from the start, and select the edge that is at the root of min-heap
Move on to that node and add all the edges again, repeat the process. We stop the alg when the no. of edges = no. of Vertices + 1
'''
from collections import defaultdict
import heapq as hq
def minCostConnectPoints(points):
    #use the index to represent the points
    l = len(points)
    adj = defaultdict(list)
    #compute the adjacency matrix
    for i in range(l):
        x1, y1 = points[i]
        for j in range(i+1, l):
            x2, y2 = points[j]
            man_dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([man_dist, j]) #for each point maintain the map of distance followed by point, dist first to put into heap
            adj[j].append([man_dist, i]) #do this for the other point as well
    #Prim's alg
    cost = 0
    visit = set()
    frontier = [[0, 0]] #start off at the 0th point, and initially add no distance to it, because we didn't add in any edge yet
    while len(visit) < l: #if this equals l, it means we touched all the points
        edge_cost, point =  hq.heappop(frontier)
        if point in visit:
            #we already touched this point, skip
            continue
        #if this is a point we didn't touch before, add its cost and mark it visited
        visit.add(point)
        cost += edge_cost
        for next_cost, next_point in adj[point]:
            if next_point not in visit:
                hq.heappush(frontier, [next_cost, next_point])
    return cost

points = [[0,0],[1,1],[1,0],[-1,1]]
print(minCostConnectPoints(points))