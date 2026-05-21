class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1+num, rob2)
            print("temp", temp)
            rob1 = rob2
            print("rob1", rob1)
            rob2 = temp
            print("rob2", rob2)
        return rob2

         
        