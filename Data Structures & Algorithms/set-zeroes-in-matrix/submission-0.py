class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        first_row_zero, first_col_zero = False, False

        # check if the first row has 0
        for c in range(col):
            if matrix[0][c] == 0:
                first_row_zero = True
                break
        # check if the first col has 0
        for r in range(row):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
        
        # use the first row / col to record other 0
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 # set the start of col = 0
                    matrix[0][c] = 0 # set the start of row = 0
        print(matrix)
        # check the first row / col to update middle part
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        print(matrix)

        if first_row_zero:
            for c in range(col):
                matrix[0][c]=0
        
        if first_col_zero:
            for r in range(row):
                matrix[r][0]=0
        
        print(matrix)
            

