class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        xAxis = {0: 0}
        position = 0
        result = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                position += 1
            elif nums[i] == 0:
                position -= 1

            if position in xAxis:
                lengthAtPosition = i - xAxis[position] + 1
                result = max(result, lengthAtPosition)
            else:
                xAxis[position] = i + 1

        return result
