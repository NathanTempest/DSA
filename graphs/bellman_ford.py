'''
Alg to find the shortest path from a single vertex to all other vertices, unlike Dijkstra's, this will work even if the edge weight
is negative. 
If there is a negative weight cycle, the alg will detect this and report that no cycle exists
The idea of atmost k stops is hard to implement with Dijkstra's, but Bellman Ford can accomodate that request
Initialize the distance from source vertex as 0 and to all other vertices as inf
Create a temp dist array that measures dist[i] from source to i
Repeat this process for v-1 times:
    - for each edge btw u, v and weight w, check if the dist to v can be shortened. If dist[u] + w < dist[v] update v
    - after v-1 iterations if the distance can still be shortened, a cycle of negative weight exists in graph
'''
def findCheapestPrice(n, flights, src, dest, k):
    prices = [float("inf")] * n
    prices[src] = 0 #intialize condn in Bellman-Ford
    
    for i in range(k+1):
        temp = prices.copy()
        for s, d, pr in flights:
            if prices[s] == float("inf"): #this source node can't even be reached at this no. of stop
                continue #skip this iteration because the source is unreachable
            if prices[s] + pr < temp[d]:
                #we compare it to temp, because the d might have already been updated by another edge in this iteration
                temp[d] = prices[s] + pr
        #all edges are touched in this iteration/no. of stops
        prices = temp #update the prices to temp so the min_price edges are put into prices

    return -1 if prices[dest] == float("inf") else prices[dest]

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(f"\n the min price to reach within {k} stops is: ", findCheapestPrice(n, flights, src, dst, k))