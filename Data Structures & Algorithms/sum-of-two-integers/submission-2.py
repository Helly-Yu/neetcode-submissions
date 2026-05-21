class Solution:
    def getSum(self, a: int, b: int) -> int:
        # xor: 1^1 = 0 1^0 = 1 0^0 = 0
        # and: 1&1 = 1 1&0 = 0 0&0 = 0    
        mask = 0xFFFFFFFF #32位掩码
        while b & mask!=0 :
            carry = (a&b) << 1
            a = (a^b) 
            b = carry
        ## 如果 a 超过了 32 位有符号整数的最大正值，说明它是负数
        return a & mask if b >0 else a


        

            
        
        

        # carry = (a&b)<<1
        # a = 4 b = 7
        # a = 0100 b = 0111
        # a^b = 0011 = a 
        # a&b = 0100 << 1 = 1000 = b 
        # a^b = 1011 = 
        # a&b = 0000 = b