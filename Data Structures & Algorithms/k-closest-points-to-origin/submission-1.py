class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #heapify 的作用是将一个已经存在且无序的完整列表，以 $O(N)$ 的复杂度一次性转换成堆。
        maxHeap = []
        for x,y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap,[dist,x,y]) # Dynamic Maintenance so no need heapq.heapify()
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
            


            
        
