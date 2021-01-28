class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        allIntervals = []
        for employee in schedule:
            for interval in employee:
                allIntervals.append(interval)

        allIntervals.sort(key=lambda x: x.start, reverse=False)
        result = []
        prev = allIntervals[0]
        for interval in allIntervals[1:]:
            if interval.start <= prev.end and interval.end > prev.end:
                prev.end = interval.end
            elif interval.start > prev.end:
                result.append(Interval(prev.end, interval.start))
                prev = interval

        return result

    # def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    #     def merge(interval1, interval2):
    #         if interval2.start <= interval1.end and interval2.end > interval1.start:
    #             start = min(interval2.start, interval1.start)
    #             end = max(interval2.end, interval1.end)
    #             consolidatedTime = Interval(start, end)
    #             return consolidatedTime
    #         return False

    #     allIntervals = []
    #     for employee in schedule:
    #         for interval in employee:
    #             allIntervals.append(interval)

    #     allIntervals.sort(key=lambda x: x.start, reverse=False)

    #     consolidated = [allIntervals.pop(0)]
    #     while allIntervals:
    #         i1 = consolidated.pop(-1)
    #         i2 = allIntervals.pop(0)
    #         merged = merge(i1, i2)
    #         if merged:
    #             consolidated.append(merged)
    #         else:
    #             consolidated.append(i1)
    #             consolidated.append(i2)

    #     result = []
    #     for i in range(0, len(consolidated)-1):
    #         interval = consolidated[i]
    #         nextInterval = consolidated[i+1]
    #         result.append(Interval(interval.end, nextInterval.start))

    #     return result
