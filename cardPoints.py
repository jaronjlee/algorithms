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
