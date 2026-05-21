class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time:o(n) space:o(1)
        profit = 0
        l = 0

        for r in range(1, len(prices)):
            # if buy > sell, move buy day to sell day
            if prices[r] < prices[l]:
                l = r
            else:
                curr = prices[r] - prices[l]
                profit = max(profit, curr)
            
        return profit



            
            