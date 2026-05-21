class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # [00]->[02] [01]->[12] [02]->[22] r=c c = 2
        # [10]->[01] [11]->[11] [12]->[21] r=c c = 1    
        # [20]->[00] [21]->[10] [22]->[20] r=c c = 0
        # Transpose
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        print(matrix)

        # reverse each row
        for r in range(n):
            matrix[r].reverse()
        
        print(matrix)
        



