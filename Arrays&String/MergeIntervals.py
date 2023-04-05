#https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:x[0])
        op = []
        startPos = intervals[0][0]
        endPos = intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0]<=endPos:
                endPos = max(intervals[i][1],endPos)
            else:
                op.append([startPos,endPos])
                startPos = intervals[i][0]
                endPos = intervals[i][1]
        op.append([startPos,endPos])

        return op