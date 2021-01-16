def minCost(cost):
    minCost = 0

    minCostArr = [[0]*3 for _ in range(0, len(cost))]
    minCostArr[0] = cost[0]

    for i in range(1, len(cost)):
        prevMinCosts = minCostArr[i-1]
        minCostArr[i][0] = cost[i][0] + min(prevMinCosts[1], prevMinCosts[2])
        minCostArr[i][1] = cost[i][1] + min(prevMinCosts[0], prevMinCosts[2])
        minCostArr[i][2] = cost[i][2] + min(prevMinCosts[0], prevMinCosts[1])

    return min(minCostArr[-1])
