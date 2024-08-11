''' Graphs
- two types either directed or undirected
- friend connections on facebook that suggest mutual friends - undirected graph
- flight routes between various cities - directed graphs
- any two nodes can be connected unlike trees
- trees are subsets of graphs
'''
import queue
import networkx as nx 
import matplotlib.pyplot as plot

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_map = {}
        for start, dest in edges:
            if start not in self.graph_map:
                self.graph_map[start] = [dest]
            #if there is already an edge from that node, simply append this to that
            else: 
                self.graph_map[start].append(dest)

    #visualize the graph
    def visualize(self):
        G = nx.DiGraph()  # Create a directed graph
        for start, dest in self.edges:
            G.add_edge(start, dest)
        pos = nx.random_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', arrows=True)
        plot.show()

    #there are two ways we can traverse the graphs, dfs and bfs
    def bfs(self, start_node):
        #track a set to avoid, showing duplicates
        visited = set()
        q = queue.Queue()
        res = []
        q.put(start_node)
        while not q.empty():
            node = q.get()
            if node not in visited:
                res.append(node)
                visited.add(node) #mark this node as visited
                for next_node in self.graph_map.get(node, []): #handles the case where a node might not be present
                    if next_node not in visited:
                        q.put(next_node)
        return res
    
    def dfs(self, start_node, visited = None):
        if visited == None:
            visited = set()
        res = []
        if start_node not in visited:
            res.append(start_node)
            visited.add(start_node)
            for next_node in self.graph_map.get(start_node, []):
                if next_node not in visited:
                    res.extend(self.dfs(next_node, visited))
        
        return res


    
    def get_path(self, start, end, path = []):
        #we don't use path += here because, it modifies the original list completely
        path = path + [start] 
        #returns a path if there is one from start to end, otherwise returns []
        if start == end:
            return [path]
        if start not in self.graph_map: #we reached a dead end
            return []
        paths = []
        for dest in self.graph_map[start]:
            if dest not in path: #only add to the path, if not already visited, avoids infinite recursion
                new_paths = self.get_path(dest, end, path)
                for p in new_paths:
                    paths.append(p)
        #if no paths are found, print that there is no path between start and dest
        return paths
    
    def get_shortest_path(self, start, dest, path = []):
        shortest_path = None
        path = path + [start] 
        if start == dest:
            return path
        if not start in self.graph_map:
            return []
        for new_start in self.graph_map[start]:
            if new_start not in path:
                new_path = self.get_shortest_path(new_start, dest, path)
                if new_path: #it may also be null, as there might not be a path from start to dest via a specific route
                    if not shortest_path or len(shortest_path) < len(new_path):
                            shortest_path = new_path
        return shortest_path
    

        

routes = [("Boston", "New York"), ("Boston", "Dallas"), ("Seattle", "San Diego"), ("Dallas", "Portland"), ("Boston", "Seattle"), 
          ("Portland", "Seattle"), ("Dallas", "Chicago"), ("Chicago", "New York"), ("Seattle", "San Diego"), ("San Diego", "Boston")]

graph = Graph(routes)
path = graph.get_path("Dulles", "San Diego")
print("\n route between Dulles and San Diego is: \n", path if path else "no such path found")
print("\n route between Boston and San Diego is: \n", graph.get_path("Boston", "San Diego"))
print("\n Shortest route between Boston and San Diego is \n", graph.get_shortest_path("Boston", "San Diego"))
print("the bfs order is", graph.bfs("Boston"))
print("the dfs order is", graph.dfs("Boston"))
graph.visualize()