def reductionCost(num):
    minCost = 0

    while len(num) > 1:
        num.sort()
        first = num.pop(0)
        second = num.pop(0)
        newNum = first + second
        minCost += newNum
        num.append(newNum)

    return minCost
