class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)

        dp[0]=1
        for coin in coins:
            ## 从这个硬币的面额开始，一直更新到目标金额
            for i in range(coin, amount+1):
                # 凑成金额 i 的方法数 = 原有的方法数 + 凑成 (i - 当前硬币面额) 的方法数
                dp[i]+=dp[i-coin]

        return dp[amount]