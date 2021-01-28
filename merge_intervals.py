class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        intervals.sort()

        result = [intervals[0]]
        for interval in intervals[1:]:
            prevInterval = result[-1]
            if interval[0] <= prevInterval[1]:
                result[-1][0] = min(prevInterval[0], interval[0])
                result[-1][1] = max(prevInterval[1], interval[1])
            else:
                result.append(interval)

        return result
