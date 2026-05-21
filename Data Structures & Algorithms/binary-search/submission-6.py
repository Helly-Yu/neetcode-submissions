class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = int((len(nums))/2)
        print(mid)
        if nums[mid]== target:
            return mid
        elif nums[mid] > target:
            while mid >= 0:
                mid-=1
                if nums[mid]== target:
                    return mid
            return -1
        elif nums[mid]<target:
            while mid < len(nums)-1:
                mid+=1
                print(mid)
                if nums[mid]== target:
                    return mid
            return -1
        