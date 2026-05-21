class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time and space: o(n)
        num_set = set(nums)
        longest_length = 0
        for n in num_set:
            if n - 1 not in num_set:
                current_num = n
                current_length = 1

                while (current_num + 1) in num_set:
                    current_num +=1
                    current_length+=1

                longest_length = max(longest_length, current_length)
        
        return longest_length
        
            
                
            
            