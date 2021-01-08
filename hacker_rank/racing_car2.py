#if next possible row == '' and prevRowPos == 'inf', change pos to min of prev row + 1
#if next possible row is '' and prevRowPos != 'inf', change pos to the prev row pos
#each space is the min number of moves it takes to get to that space
#return min of the top row of the grid


# ['inf', 2,   1],
# [2,   2, 'inf'],
# ['', 'inf', ''],
# [2,   2, 'inf'],
# ['inf', 2,   1],
# [1,   'inf', 1],
# [1,    0,    1]
# [2,    1,    2]

def minimumMoves(obstacleLanes):
  grid = [[""] * 3 for _ in range(len(obstacleLanes))]

  for i in range(len(obstacleLanes)):
    grid[i][obstacleLanes[i]-1] = float("inf")

  grid.insert(0, [1, 0, 1])

  for i in range(1, len(grid)):
    for j in range(0, 3):
      currentRow = grid[i]
      currentPos = currentRow[j]
      prevRow = grid[i-1]
      prevPos = prevRow[j]

      if prevPos == float("inf") and currentPos == "":
        grid[i][j] = min(prevRow) + 1
      elif prevPos != float("inf") and currentPos == "":
        grid[i][j] = prevPos

  return min(grid[-1])


x = [2, 1, 2]
y = [2, 1, 3, 2, 2]
z = [2, 1, 3, 2, 3, 1]

print(minimumMoves(z))

#   X
#   X
#     X
# X
#   X
# 1 2 3
