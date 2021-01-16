# def getMaxColors(prices, money):
#     totalSum = sum(prices)
#     L = 0
#     R = len(prices)-1
#     incrementR = 1
#     previousRightSum = 0
#     leftSum = 0
#     rightSum = 0
#     while L < R:
#         currentSum = totalSum - leftSum - rightSum
#         if currentSum > money and R == len(prices)-1:
#             L = 0
#             leftSum = 0
#             R -= incrementR
#             rightSum += prices[R+1] + previousRightSum
#             previousRightSum = rightSum
#             incrementR += 1
#         elif currentSum > money:
#             leftSum += prices[L]
#             rightSum -= prices[R+1]
#             L += 1
#             R += 1
#         elif currentSum <= money:
#             return R - L + 1
#     print(L)
#     print(R)
#     if L == R and prices[0] <= money:
#         return 1
#     return 0


def getMaxColors(prices, money):
    maxWindow = 0
    boolean = True

    while boolean:
        boolean = False
        for i in range(len(prices)-maxWindow):
            subArray = prices[i:i + max + 1]
            sumArray = sum(subArray)
            if sumArray <= money:
                boolean = True
                maxWindow += 1
                break

    return maxWindow
