# https: // leetcode.com/discuss/interview-question/221639/

# Description
# A company wants to develop an office park in an area that has been divided up into a grid. 
# Each cell represents a potential building lot. The goal is for the furthest of all lots to be as 
# near as possible to an office building. Determine the building placement to minimize the distance of 
# the most distant lot from an office building. Movement is restricted to horizontal and vertical. 
# Diagonal movement is not allowed.

# Example
# w = 4
# h = 4
# n = 3

# There are n = 3 office buildings to build on a grid that is w = 4 lots wide and h = 4 lots high. 
# An optimal grid placement sets any lot within two units distance of an office building. 
# In the distance grid below, offices are cells at distance 0.

# 1 0 1 2
# 2 1 2 1
# 1 0 1 0
# 2 1 2 1

# This represents one optimal solution among several. The array could be rotated for another optimal solution.

# Function Description
# Complete the function findMinDistance in the editor below.
# findMinDistance has the following parameters(s):

# int w: the width of the grid
# int h: the height of the grid
# int n: the number of buildings to place

# Returns:
# int: the maximum value among shortest distances to the closest office for each cell



#PSUEDO CODE
#make array of tuples for every position and the third element in the tuple = 0
#get all combinations from that array of length n where n is the number of office buildings. this is an array [(0, 0, 0), (0, 1, 0), (0, 2, 0)]
#iterate through all combinations
#for each combination, create queue. Then iterate throguh the combination and 
#   add each position to the queue (representing office buildings)
#   add each position to a visited set()
#   while queue:
#       pop left element in queue
#       set a distance variable to the max of (current distance, distance)
#       iteratate through directions (up down left right) and 
#       if within bounds and pos not visited:
#           append (x, y, dist+1) to queue  
#           add (x,y) to visited)
#   update maxDistance


# import itertools
# from collections import deque

# def buildOffice(height, width, n):
#     arr = []
#     for i in range(height):
#         for j in range(width):
#             arr.append((i, j, 0))

#     ans = float("inf")
#     for points in itertools.combinations(arr, n):
#         q = deque([])
#         visited = set()
#         for m, n, dist in points:
#             q.append((m, n, dist))
#             visited.add((m, n))
#         distAns = 0
#         while q:
#             i, j, dist = q.popleft()
#             distAns = max(dist, distAns)
#             for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
#                 if 0 <= x < height and 0 <= y < width and (x, y) not in visited:
#                     q.append((x, y, dist+1))
#                     visited.add((x, y))
#         ans = min(distAns, ans)

#     return ans


import itertools

def findMinDistance(w, h, n):
  minDistance = float('inf')

  allPositions = []
  for row in range(h):
    for col in range(w):
      # get all pos with buildings as 3rd item in array
      allPositions.append((row, col, 0))

  # get combinations of 3 office buildings
  combinations = itertools.combinations(allPositions, n)

  for combination in combinations:
    # print(f'combination {combination}')
    queue = []
    visited = set()

    for r, c, dist in combination:
      queue.append([r, c, dist])
      visited.add((r, c))

    maxClosestDist = 0
    while queue:
      r, c, dist = queue.pop(0)
      # print([r, c, dist])
      maxClosestDist = max(dist, maxClosestDist)
      for x, y in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
        if 0 <= x < h and 0 <= y < w and (x, y) not in visited:
          queue.append([x, y, dist+1])
          visited.add((x, y))

    minDistance = min(maxClosestDist, minDistance)
    # print(f'visited = {visited}')

  return minDistance


print(findMinDistance(7, 7, 2))
