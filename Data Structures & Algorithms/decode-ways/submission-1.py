class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0': return 0
        
        prev2, prev1 = 1, 1 # 分别对应 dp[i-2] 和 dp[i-1]
        
        for i in range(1, len(s)):
            current = 0
            # 一位数情况
            if s[i] != '0':
                current += prev1
            # 二位数情况
            two = int(s[i-1:i+1])
            if 10 <= two <= 26:
                current += prev2
            
            if current == 0: return 0 # 无法继续解码
            
            prev2 = prev1
            prev1 = current
            
        return prev1