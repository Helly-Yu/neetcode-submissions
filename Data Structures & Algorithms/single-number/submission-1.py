class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR? sum? 
        res = 0
        for num in nums:
            print(num)
            res = num^res # 011 ^ 000= 011, 010^011 = 001, 011^001 = 010
            print(res)
        return res
        


        