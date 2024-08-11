'''
Kruskal's algorithm to find the mininum spanning sub-tree, makes use of union find to find the disjointed set union.
This DS can handle connected components neatly and help us identify connected components.
- Find: Determines which set a particular element belongs to. This operation can be optimized 
    using path compression to flatten the structure, speeding up future operations.
- Union: Merges two disjoint sets into a single set. This can be optimized using union by 
    rank or union by size to ensure the tree representing the sets remains shallow.
The minimum spanning tree, forms the connections with the least cost.
The steps involved are:
    - Sort edges by ascending edge weight
    - Walk through these sorted edges and look at the two nodes in the edges, if they are already unified, we skip the edge.
    - Otherwise we include these edges and unify those nodes.
    - The algorithm terminates when every edge has been processed or all vertices are unified.
'''
