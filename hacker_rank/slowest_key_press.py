def slowestKey(keyTimes):
    alpha = "abcdefghijklmnopqrstuvwxyz"

    longestIdx = 0
    longestTime = keyTimes[0][1] - 0

    for i in range(1, len(keyTimes)):
        index, currentTime = keyTimes[i]
        prevTime = keyTimes[i-1][1]
        diff = currentTime - prevTime
        if diff > longestTime:
            longestIdx = index
            longestTime = diff

    return alpha[longestIdx]
