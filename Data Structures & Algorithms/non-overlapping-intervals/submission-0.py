class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) # sort by the end time
        prevEnd = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count+=1

            # if intervals[i][0] >= prevEnd:
            #     prevEnd = intervals[i][1]
            # else:
            #     count+=1
            #     prevEnd = min(prevEnd, intervals[i][1])
        
        return count
                
