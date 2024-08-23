class Solution:
    def totalNQueens(self, n: int) -> int:
        if n in [2,3]:
            return 0
        elif n == 1:
            return 1
        #initialize the board
        self.res = 0
        #we dont need row_set as the backtracking function allows only one queen per row
        col_set = set()
        posdiag = set()
        negdiag = set()

        def backtrack(r):
            if r == n:
                #happy case, incr res by 1
                self.res += 1
                return
            #we did not place all of the n queens
            #we can place a queen on a col in this row
            for c in range(n):
                if c in col_set or (r+c) in posdiag or (r-c) in negdiag:
                    #it means that the queen in this column is under attack, skip to go to the next column
                    continue
                #if we could place a queen in a column that is not under attack
                col_set.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                backtrack(r+1) #we successfully placed a queen on this row, move on to the next
                #this above function has two possibilities, either it can run till all rows are done, or it will fail.
                #the for loop still might have some column values that we could try
                col_set.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                #so we reset the board to what it was before this column, go back one level in case of failure, or success too as there might be
                #multiple values of columns for our answers
        backtrack(0)
        return self.res
sol = Solution()
print(sol.totalNQueens(11))