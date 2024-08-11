class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None #initialize both the pointers to null

    def insert(self, value):
        #insert in such a way that the node is greater than all the elements in the left tree, and smaller than all the elements in the
        #right tree
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def bfs(self):
        tree = []
        q = [self]
        while(q):
            node = q.pop(0)
            if node:
                tree.append(node.value)
                q.append(node.left)
                q.append(node.right)
        return tree

    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal() #do this until we reach the left-most node, and print its value

        if self.right:
            self.right.preorder_traversal() #prints the right-most node
    
    def search(self, value):
        if value < self.value:
            #search in the left sub-tree, if it is not empty
            if not self.left:
                return False
            else:
                return self.left.search(value)
        elif value > self.value:
            #search in the right sub-tree, if it is not empty
            if not self.right:
                return False
            else:
                return self.right.search(value)
        else: #the value is the same as the current
            return True

tree = TreeNode(3)
tree.insert(4)
tree.insert(-1)
tree.insert(14)
tree.insert(9)
print("bfs traversal", tree.bfs())
tree.preorder_traversal()
print("searching for non-existing node : ")
print(tree.search(-5))
print("searching for existing node : ")
print(tree.search(14))
