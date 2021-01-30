class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        result = len(nums)+1
        runningSum = 0
        L = 0
        R = 0

        while R < len(nums):
            runningSum += nums[R]
            while runningSum >= s:
                result = min(result, R-L+1)
                runningSum -= nums[L]
                # print(result)
                # print(runningSum)
                L += 1
            R += 1

        if result < len(nums)+1:
            return result
        else:
            return 0
