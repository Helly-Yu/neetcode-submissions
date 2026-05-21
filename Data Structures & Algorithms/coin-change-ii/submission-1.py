class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. 初始化 DP 数组
        # dp[i] 表示凑成金额 i 的方法数
        dp = [0] * (amount + 1)
        
        # 2. 基础情况：凑成 0 元的方法只有 1 种（什么都不拿）
        dp[0] = 1
        
        # 3. 核心逻辑：先遍历硬币 (Outer Loop)
        for coin in coins:
            # 再遍历金额 (Inner Loop)
            # 从这个硬币的面额开始，一直更新到目标金额
            for i in range(coin, amount + 1):
                # 状态转移方程：
                # 凑成金额 i 的方法数 = 原有的方法数 + 凑成 (i - 当前硬币面额) 的方法数
                dp[i] += dp[i - coin]
                
        return dp[amount]