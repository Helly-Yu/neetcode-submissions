class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        pre = 1 if x >= 0 else -1
        x = abs(x)

        while x!=0:
            pop = x % 10
            x = x // 10
            
            if pre == 1:
                if res > MAX // 10 or (res == MAX // 10 and pop > MAX % 10):
                    return 0
            else:
                if res > abs(MIN //10) or (res == abs(MIN // 10) and pop > abs(MIN %10)):
                    return 0 
            res = (res * 10) + pop
        return res * pre
        
            

        



        # 123%10= 3    3*10. 3*10*10
        # 123/10 = 12
        # 12% 10 = 2.        2*10
        # 12/10 = 1
        # 1%10 = 1             1
        # 1/10 =0         
        
        
        