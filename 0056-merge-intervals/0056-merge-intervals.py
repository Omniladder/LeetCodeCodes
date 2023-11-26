class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = []
        outputList = []
        temp = intervals[0][0]
        for i in range(len(intervals) - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                outputList.append([temp ,intervals[i][1]])
                temp = intervals[i+1][0]
            elif intervals[i][1] > intervals[i + 1][1]:
                intervals[i + 1][1] = intervals[i][1]
        outputList.append([temp ,intervals[len(intervals) - 1][1]])
        return outputList