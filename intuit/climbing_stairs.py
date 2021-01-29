class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1
        curr = 2

        for i in range(2, n):
            temp = prev + curr
            prev = curr
            curr = temp

        return curr


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 2

#         ways = [0]*n
#         ways[0] = 1
#         ways[1] = 2

#         for i in range(2, n):
#             ways[i] = ways[i-1] + ways[i-2]

#         return ways[-1]


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2

#         dp = [1, 2]
#         length = 2
#         while length < n:
#             dp.append(dp[-1]+dp[-2])
#             length += 1

#         return dp[-1]
