#depth-first search

#three ways to process - pre, in, and post-order
#pre-order is when a print a node before its children
#in-order is w
#post-order is when a node is processed after all its children have been exhausted

#can do this recursively using stacks - slower or iteratively using our own call stack

class Node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left  = left
        self.right = right

#both the methods are used to implement pre-order traversal
def dfs_traverse_rec(tree):
    if tree is not None:
        print(tree.val)
        dfs_traverse_rec(tree.left)
        dfs_traverse_rec(tree.right)

def dfs_traverse_iter(tree):
    stack = []
    stack.append(tree)
    while stack:
       node = stack.pop()
       if node:
           print(node.val)
           stack.append(node.right)
           stack.append(node.left)

tree_sample = Node(2, Node(3, Node(4)), Node(5, Node(7), Node(8)))
print("the pre-order of dfs recursively : ")
dfs_traverse_rec(tree_sample)
print("\n the pre-order of dfs iteratively : ")
dfs_traverse_iter(tree_sample)

#bfs refers to printing all the nodes of a level
#we use a queue instead of a stack to implement this


def bfs_traverse_iter(tree):
    queue = []
    queue.append(tree)
    while queue:
        if queue:
            node = queue.pop(0)
            if node:
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)

print("the bfs pre-order traversal : ")
bfs_traverse_iter(tree_sample)
