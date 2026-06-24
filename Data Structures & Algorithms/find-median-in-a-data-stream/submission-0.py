import statistics
class MedianFinder:

    def __init__(self):
        # store negative numbers, max heap
        self.small = []
        # store positive numbers, min heap
        self.large = []
        

    def addNum(self, num: int) -> None:
        # time: O(logn)
        heapq.heappush(self.small, -num)
        # make sure the number in small <= the number in large
        if self.small and self.large and (-self.small[0]> self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # make sure the ammount difference <= 1
        if len(self.small)> len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # time: o(1)
        if len(self.small)> len(self.large):
            return float(-self.small[0])
        
        return (-self.small[0]+self.large[0])/2.0
        

       

        