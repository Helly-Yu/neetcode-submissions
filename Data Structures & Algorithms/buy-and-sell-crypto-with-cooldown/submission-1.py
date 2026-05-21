class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        hold = -prices[0] # hold one coin
        sold = 0 # sold today
        rest = 0 # no money and no sold 

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            # 1. 持有：要么继续持有，要么在休息后买入
            hold = max(prev_hold, prev_rest - price) 
            # 2. 卖出：只能从持有状态卖出
            sold = prev_hold + price
            # 3. 休息：要么继续休息，要么是刚卖完进入冷冻
            rest = max(prev_rest, prev_sold)
            print(hold, sold, rest)
        
        return max(sold, rest)
        

            
