class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time: O(m * (4^n)) space:o(n)
        rows, cols = len(board), len(board[0])

        # r: row, c:cols, i: i-th char in the word
        def dfs(r, c, i):
            # success:
            if i == len(word):
                return True
            
            # fail:
            if (r<0 or c<0 or r>=rows or c>=cols or board[r][c]!=word[i]):
                return False

            temp = board[r][c]
            # mark 
            board[r][c]= '#'  
            # explore four direction 
            res = (dfs(r+1, c, i+1) or # down
                    dfs(r-1, c, i+1) or # up
                    dfs(r, c+1, i+1) or # right
                    dfs(r, c-1, i+1)) # left
                
            
            board[r][c] = temp
            return res
        # Find the start 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False

