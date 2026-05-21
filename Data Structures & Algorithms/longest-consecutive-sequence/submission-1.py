class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: # 总体时间复杂度：$O(n) + O(n) + O(n) = O(n)$
        numSet=set(nums) # 建立 numSet：$O(n)$ 
        longest = 0
        for n in nums: #外部循环：$O(n)$
            print("n:", n)
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet: # 所有 while 循环的总执行次数：$O(n)$（因为每个元素最多进一次 while）
                    length+=1
                longest = max(length, longest)
            print(longest)
        return longest
