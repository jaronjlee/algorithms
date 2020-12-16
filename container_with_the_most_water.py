class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1, p2 = 0, len(height)-1
        max_water = 0
        while p1 < p2:
            water = min(height[p1], height[p2]) * (p2 - p1)
            if max_water < water:
                max_water = water

            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_water
