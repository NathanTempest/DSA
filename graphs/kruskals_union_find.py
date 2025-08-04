class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        In an undirected graph, we use the union find to detect cycles. Initially set all
        parents to itself and gradually update it, whenever we detect a cycle return that edge
        '''
        n = len(edges)
        parent = list(range(n+1))

        '''union find has two functions find and union, union groups two cells if they have the same
        parent. Find helps to find a root parent for each vertex'''

        
        def union(v1, v2):
            p1, p2 = parent[v1], parent[v2]
            #if both vertices have the same parent, that means a union has just formed at this edge
            if p1 == p2:
                return False
            #these edges do not have the same parent, so update the parent
            parent[p2] = p1
            return True
        
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]