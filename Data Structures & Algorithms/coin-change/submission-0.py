class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1]*(amount+1)

        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                # # 只有当当前金额大于等于硬币面额时，才能尝试使用这枚硬币
                if i-coin>=0:
                    print(i, coin, dp[i-coin])
                    # 决策：[保持现状] vs [用这一枚硬币 + 凑齐剩余金额所需的最少硬币]
                    dp[i]=min(dp[i], 1+dp[i-coin])
                    print(dp[i])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1