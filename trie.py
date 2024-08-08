#useful for doing things like autofilling, tries are also referred to as prefix trees
#in the case of deletion, we cannot delete the node if it has children in a tree. If the word exists and it has children, we just set
#its indicator to False.
#if a word say cat is in the trie, its leaf shows it to be true, but if we are searching for ca, it doesn't point its true, even if cat exists
class TrieNode:

    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] #move the word along until we reach the word end
        node.word_end = True
    
    #if we remove words from the trie after we're done with them, we can make our code faster
    def remove(self, word):
        def delete(node, word, depth):
            #we only delete a node, in case of True values.
            if depth == len(word):
                #break case for recursion, if the word is not an end_word, return False
                if not node.word_end: #the word is not found
                    return False
                #Unmark the word end, because its deleted
                node.word_end = False
                return len(node.children) == 0 #it can still have children and be undeletable
            char = word[depth] #if this character is not in node's children, its pointless to delete as
            #the word either doesn't exist or unreachable from here
            if char not in node.children:
                return False
            #its deletable in case, its not a word_end and doesn't have children
            deletable = delete(node.children[char], word, depth+1) #check dfs-ly to remove nodes from end 
            #till here
            if deletable:
                del node.children[char]
                return len(node.children) == 0 #this node can still have other children, return False as to
                #not delete it in that case, but we would still unmark the word_end above
            #if the deletable returned False, down the dfs, either the word is still a word_end or some nodes
            #have children
            return False #undeletable
        delete(self, word, 0)
            
            
class Solution:
    def findWords(self, board, words):
        #intialize the result to hold unique words, the path to avoid infinite recursion
        res, path = set(), set()
        ROW, COL = len(board), len(board[0])
        self.root = TrieNode()

        for word in words:
            node = self.root
            node.insert(word) #build a trie with all the words
        
        def backtrack(r, c, node, curr_word):
            #break for out of bounds
            if r < 0 or r >= ROW or c < 0 or c >= COL or (r,c) in path or board[r][c] not in node.children:
                #board char not in node children implies that the wanted word cannot be formed from the curr node
                return
            #if the board character however can be reached from the current node's children, it means that 
            #the word can proceed to form for another step
            path.add((r,c))
            node = node.children[board[r][c]]
            curr_word += board[r][c]
            if node.word_end:
                res.add(curr_word)
                #also remove this word from the trie, so as to not compute and add it to the set again
                self.root.remove(curr_word)
            backtrack(r+1, c, node, curr_word)
            backtrack(r-1, c, node, curr_word)
            backtrack(r, c-1, node, curr_word)
            backtrack(r, c+1, node, curr_word)
            path.remove((r,c))
        for r in range(ROW):
            for c in range(COL):
                backtrack(r, c, self.root, "")
        return list(res)


sol  = Solution() #creates an object of the Trie class, feel free to use all its methods
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
res = sol.findWords(board, words)
print(res)