class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1]< newInterval[0]:
            # 1. left no overlap zone 
            res.append(intervals[i])
            i+=1

        # 2. overlap: i.start <= new.end
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        
        res.append(newInterval)

        # 3. add the right no overlap zone:
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res