class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # Extend the existing subarray sum by adding the current element.
        # Start fresh with the current element (if the previous sum was dragging you down).

        curr_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(curr_sum, max_sum)
            print(curr_sum, max_sum)
        return max_sum