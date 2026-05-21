class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #d[i][j] means s1[:i] + s2[:j] => s3[:i+j]
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        # the first row
        for i in range(1, m+1):
            dp[i][0]= dp[i-1][0] and s1[i-1] == s3[i-1]
        # the firts col
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
                print(f"dp[{i}][{j}]:", dp[i][j])
        return dp[m][n]