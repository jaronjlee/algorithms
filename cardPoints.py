# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)

        if k == len(cardPoints):
            return totalSum

        minSum = float('inf')
        runningSum = 0

        l = 0
        r = 0
        windowLength = len(cardPoints) - k
        while r < len(cardPoints):
            runningSum += cardPoints[r]

            if r - l + 1 == windowLength:
                minSum = min(runningSum, minSum)
                runningSum -= cardPoints[l]
                l += 1

            r += 1

        return totalSum - minSum

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        totalSum = sum(cardPoints)

        if k == len(cardPoints):
            return totalSum

        windowLength = len(cardPoints)-k  # 4
        tempSum = sum(cardPoints[0:windowLength])  # 22
        minSum = tempSum  # 10

        for i in range(1, len(cardPoints)-windowLength+1):
            tempSum -= cardPoints[i-1]
            tempSum += cardPoints[i+windowLength-1]
            minSum = min(minSum, tempSum)

        # print(minSum)
        return totalSum - minSum
