class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use similar algorithm as 2sum II
        # build a outer loop, to reach the uniqueness requirement, whenver encounter a same element, jump and consider next element.
        # for inner loop, use two pointer strategy. one pointer starts from left, the other one from right
        # but for inner loop, how to meet the uniqueness requirement? The uniqueness could not be reached if there are repeated numbers
        # and since we have sorted the list, these repeated numbers are adjacent, so use a flag to consider this situation.
        if len(nums) <= 2:
            return []
        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            else:
                j = i + 1
                k = len(nums) - 1
                target = -nums[i]
                flag = 1
                while j < k:
                    if nums[j] + nums[k] > target:
                        k -= 1
                        flag = 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                        flag = 1
                    else:
                        if flag == 1:
                            ret.append([nums[i], nums[j], nums[k]])
                            flag = 0
                        else:
                            pass
                        k -= 1

        return ret
