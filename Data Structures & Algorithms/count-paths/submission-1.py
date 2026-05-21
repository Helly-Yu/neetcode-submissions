class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #2d: dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        dp = [[1]*n for _ in range(m)] # m*n 
        for i in range(1,m):
            for j in range(1,n):
                # 到达当前格子的路径 = 上边来的 + 左边来的
                dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        
        return dp[m-1][n-1]


        

        