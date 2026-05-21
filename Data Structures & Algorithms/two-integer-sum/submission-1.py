class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time o(n) and space o(n)
        hash_table = {}
        for i, n in enumerate(nums):
            difference = target - n
            # if diff has already stored in hash table => the index of diff is smaller than the current index
            if difference in hash_table:
                return[hash_table[difference], i]
            # else, store the num in hash table
            hash_table[n]=i
            
            

            

        
        
        
            
