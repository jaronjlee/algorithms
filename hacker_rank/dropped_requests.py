from collections import defaultdict


def droppedRequests(requestTime):
    transactionsPerSecond = defaultdict(int)
    for time in requestTime:
        transactionsPerSecond[time] += 1
    rollingTen = 0
    countTen = 0  # 10
    rollingSixty = 0
    countSixty = 0
    dropped = 0
    for i in range(1, requestTime[-1]+1):  # range 1:8
        seconds = i
        numTransactions = transactionsPerSecond[seconds]
        if numTransactions > 3:
            dropped += numTransactions-3
        if countTen < 10:
            rollingTen += numTransactions
            countTen += 1
        if countSixty < 60:
            rollingSixty += numTransactions
            countSixty += 1
        if countTen >= 10:
            rollingTen += numTransactions
            rollingTen -= transactionsPerSecond[i-10]
        if countSixty >= 60:
            rollingSixty += numTransactions
            rollingSixty -= transactionsPerSecond[i-60]
        if rollingTen > 20:
            dropped += rollingTen - 20
        if rollingSixty > 60:
            dropped += rollingSixty - 60
    return dropped
