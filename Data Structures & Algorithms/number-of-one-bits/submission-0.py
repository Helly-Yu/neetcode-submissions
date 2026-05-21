class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        for i in range(32): 
            mask = 1 << i # mask = 1 << i 循环 32 次，每次生成一个只在第i位是1的数字
            if mask & n :
                res += 1
            
        return res

            
        