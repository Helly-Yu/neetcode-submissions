class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(N*M)
        # n = len(matrix) # row
        # m = len(matrix[0]) # col
        # for r in range(n):
        #     start = matrix[r][0]
        #     end = matrix[r][m-1]
        #     if target >= start and target <= end:
        #         for c in range(m):
        #             print(matrix[r][c])
        #             if target == matrix[r][c]:
        #                 return True
        # return False
        rows = len(matrix)
        cols = len(matrix[0])
        l, r =0, rows * cols-1
        while l <= r:
            m = (l + r) // 2
            row = m // cols
            col = m % cols
            print(m,row,col)
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False




            

        
