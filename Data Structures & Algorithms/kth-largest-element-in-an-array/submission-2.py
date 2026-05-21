class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap = []
        # for num in nums:
        #     heapq.heappush(maxHeap, -num)
        #     if len(maxHeap) > len(nums) - k + 1:
        #         heapq.heappop(maxHeap)
        
        # return -heapq.heappop(maxHeap)
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]


