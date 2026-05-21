class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # row
        m = len(matrix[0]) # col
        for r in range(n):
            start = matrix[r][0]
            end = matrix[r][m-1]
            if target >= start and target <= end:
                for c in range(m):
                    print(matrix[r][c])
                    if target == matrix[r][c]:
                        return True
        
        return False
            

        
