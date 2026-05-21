class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-k for k in stones]
        heapq.heapify(max_heap) # top one is the bigest one
        while len(max_heap)>1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first == second:
                continue
            elif first > second:
                val = first-second
                heapq.heappush(max_heap, -val)
        
        return 0 if len(max_heap) == 0 else -max_heap[0]