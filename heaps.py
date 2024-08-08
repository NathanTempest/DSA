'''
- Heaps are defined in the heapq library in python, used to order elements based on their priority. It is a tree data structure.
- Lists are converted to heaps in linear time
- A min heap is when the children of a node are always greater than itself, and max heap is the inverse.
- For a node at index i, the first child is at 2*i + 1, second child is at 2*i + 2
- To implement max heap, just turn every element to negative, we have a min heap but its value when turned +ve would represent max heap
'''
import heapq as h
data = [2, 22, 33, 44, 5, 129, 19, 9, 0]
d1 = sorted(data) #this wouldn't be enough because inserting and updating takes O(n), heap can insert it at the end and perform heapify
                    #reducing this time to O(log(n))
print("\n sorted", d1)
h.heapify(data)
min_heap = data
print("\n min heap", min_heap)
#pop the first element and see the heap re-organize
print("\n popped the first element", h.heappop(data))
print("\n reorganized heap", data)
h.heappush(data, -11)
print("\n pushed heap", data)
#could also use an undocumented max heap functions
h._heapify_max(data)
max_heap = data
print("\n max heap", max_heap)



