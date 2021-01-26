class Solution:
    def maxArea(self, height) -> int:
        result = 0

        left = 0
        right = len(height)-1

        while left < right:
            length = right - left
            currentArea = length * min(height[left], height[right])
            result = max(result, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
