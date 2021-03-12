def widestGap(n, start, finish):
    intervals = []
    for i in range(0, len(start)):
        intervals.append([start[i], finish[i]])
    intervals.sort()
    minInterval = min(intervals)
    mergedIntervals = [minInterval]
    for interval in intervals[1:]:
        if interval[0] <= mergedIntervals[-1][1]:
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1])
        else:
            mergedIntervals.append(interval)
    result = 0
    if mergedIntervals[0][0] > 0:
        result = mergedIntervals[0][0] - 1
    for i in range(0, len(mergedIntervals)-1):
        result = max(
            result, mergedIntervals[i+1][0] - mergedIntervals[i][1] - 1)
    if mergedIntervals[-1][1] < n:
        result = max(result, n - mergedIntervals[-1][1])
    return result
