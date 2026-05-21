class Solution:
    def reverseBits(self, n: int) -> int:
        # 01 << 1 = 10
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # Extract the i-th bit of n， 第 i 位“挤”到最低位； 如果最后一位是 1，结果就是 1；如果是 0，结果就是 0
            res |= (bit << (31 - i)) # Shift this bit to position (31 - i)
        return res

        # 4, n= 0101
        # i = 0, 1, 2, 3
        # bit = 0101 & 1 = 1, 0010 & 1 = 0, 0001 & 1= 1, 0000&1=0
        # bit <<(3-i) = 1 << 3(1000), 0<<2(0000), 1<<1(0010), 0<<0(0000)
        # res = 0
        # res | 1000 = 1000, 1000|0000 = 1000, 1000|0010= 1010, 1010|0000 = 1010

            
            