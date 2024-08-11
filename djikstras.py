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
    