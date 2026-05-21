class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # #2d: dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        # dp = [[1]*n for _ in range(m)] # m*n 
        # for i in range(1,m):
        #     for j in range(1,n):
        #         # 到达当前格子的路径 = 上边来的 + 左边来的
        #         dp[i][j] = dp[i-1][j]+ dp[i][j-1]
        
        # return dp[m-1][n-1]
        dp=[1]*n
        for i in range(m-2, -1, -1):
            for j in range(n-2,-1,-1):
                dp[j]+=dp[j+1]
                print(dp[j])
        return dp[0]


        

        