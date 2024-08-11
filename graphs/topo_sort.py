'''
Topological Sort is the ordering of the vertices in a Directed Acyclic Graph in a way that there is an order followed by the vertices.
It helps us to determine the course of actions taken one after the other. It can only be done if the graph has no cycles. There can be
multiple valid topo sorts for the same graph. Leetcode - 207
'''
from collections import deque
def topo_sort(n, edges_list):
    in_edges = [0] * n #refers to the total number of edges coming into the node, the edge [1,2] represents edge from 2 - 1
    adj_list = [[] for x in range(n)]
    print(adj_list)
    for e in edges_list:
        adj_list[e[1]].append(e[0])
        in_edges[e[0]] += 1 #we spotted an edge coming into this node, so increment it
    q = deque()
    for i in range(n):
        if in_edges[i] == 0:
            q.append(in_edges[i]) #add all the nodes to the queue that do not have any edges coming in.
    #track a variable visited that helps us track how many nodes were visited
    visited = 0
    while q:
        node = q.popleft()
        visited += 1 #we only try to visit the nodes that have 0 in_edges, we can spot the cycles, because some node can't be visited
        for next_node in adj_list[node]:
            in_edges[next_node] -= 1
            if in_edges[next_node] == 0:
                q.append(next_node)
    return n == visited

n = 4
edges_list = [(1, 0), (2, 1), (3, 2)]
print(topo_sort(n, edges_list))

n = 4
edges_list = [(0, 1), (1, 2), (2, 3), (3, 1)]
print("\n Has an edge should return False : ")
print(topo_sort(n, edges_list))

n = 3
edges_list = []
print("no edges in this graph, should return True because it means that the graph has no edges")
print(topo_sort(n, edges_list))

