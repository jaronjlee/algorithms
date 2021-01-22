# Given an integer array A[ ] of size N, the task is to find a subsequence of size B such that the minimum difference between any two of them is maximum and print this largest minimum difference.

# Input: A[ ] = {1, 2, 3, 5}, B = 3
# Output: 2
# Explanation:
# Possible subsequences of size 3 are {1, 2, 3}, {1, 2, 5}, {1, 3, 5} and {2, 3, 5}.
# For {1, 3, 5}, possible differences are (|1 – 3| = 2), (|3 – 5| = 2) and (|1 – 5| = 4), Minimum(2, 2, 4) = 2
# For the remaining subsequences, the minimum difference comes out to be 1.
# Hence, the maximum of all minimum differences is 2.

import itertools


def maxMinDifference(arr, b):
  maxMinDiff = float("-inf")

  for combination in itertools.combinations(arr, b):
    minDiff = minDifference(combination)
    maxMinDiff = max(maxMinDiff, minDiff)

  return maxMinDiff


def minDifference(tup):
  arr = sorted(tup)
  minDiff = float("inf")
  for i in range(0, len(arr)-1):
    minDiff = min(minDiff, abs(arr[i+1]-arr[i]))

  return minDiff

# print(minDifference((6,1,3)))


a = [5, 17, 11]
b = 2  # subsequence size

print(maxMinDifference(a, b))
