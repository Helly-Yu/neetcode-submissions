class Solution:
    def findMin(self, nums: List[int]) -> int:
        # time: o(logn) space: o(n)
        # find the minimum number
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2
            
            # If mid is greater than the right pointer, the min is to the right
            if nums[mid] > nums[r]:
                l = mid + 1
                
            # If mid is less than or equal to the right pointer, the right side is sorted.
            # The min is at mid or to the left of mid.
            else:
                r = mid
        
        # When the loop terminates (l == r), we have found the minimum element
        return nums[l]
            
            

            



