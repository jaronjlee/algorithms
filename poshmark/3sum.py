class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        resultSet = set()
        nums.sort()

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum < 0:
                    j += 1
                elif currentSum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1

        return result
