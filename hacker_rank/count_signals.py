def countSignals(frequencies, filterRanges):
    # Write your code here
    minNum = filterRanges[0][0]
    maxNum = filterRanges[0][1]
    count = 0
    for i in range(1, len(filterRanges)):
        x = filterRanges[i][0]
        y = filterRanges[i][1]
        minNum = max(minNum, x)
        maxNum = min(maxNum, y)
    for frequency in frequencies:
        if frequency in range(minNum, maxNum+1):
            count += 1
    return count