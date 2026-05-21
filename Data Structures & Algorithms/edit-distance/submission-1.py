class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # d[i][j] word1[:i] == word2[:j] minimum operiations
        m = len(word1)
        n = len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0]= 0
        # base cases: 当其中一个单词为空时
        for i in range(1,m+1):
            dp[i][0] = i # word1 变成空字符串：全部删除
        
        for j in range(1,n+1):
            dp[0][j]= j # 空字符串变成 word2：全部插入
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j]= min(dp[i-1][j-1]+1,  # replace word1[i-1] to word2[j-1]
                    dp[i-1][j]+1, # delete word1[i-1]
                    dp[i][j-1]+1) # insert after word[i-1]
                    
        
        return dp[m][n]