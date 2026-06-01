class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time:o(logn) space:o(n)

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            
            # if Left is sorted:
            if nums[l] <= nums[mid]:
                # Is the target within the strict bounds of this sorted left half?
                if nums[l] <= target <nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # if right is sorted
            else:
                # Is the target within the strict bounds of this sorted right half?
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            
        
        return -1

        