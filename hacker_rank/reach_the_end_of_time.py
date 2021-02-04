#DFS
def reachTheEnd(grid, maxTime):
    def dfs(row, col, height, width, visited, time):
        if row == height - 1 and col == width - 1 and time <= maxTime:
            return True
        if time > maxTime:
            return False

        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newX = row + x
            newY = col + y
            if newX >= 0 and newX < height and newY >= 0 and newY < width and \
                    grid[newX][newY] == "." and visited[newX][newY] == False:
                visited[newX][newY] = True
                if dfs(newX, newY, height, width, visited, time+1):
                    return True
                visited[newX][newY] = False

        return False

    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    visited[0][0] = True
    height = len(grid)
    width = len(grid[0])
    if dfs(0, 0, height, width, visited, 0):
        return "Yes"
    else:
        return "No"


#BFS
# def reachTheEnd(grid, maxTime):
#     visited = [[False] * len(grid[0]) for _ in range(len(grid))]
#     queue = [[0,0]]
#     count = 0
#     height = len(grid)
#     width = len(grid[0])

#     while queue:
#         currentMoves = len(queue)
#         if count > maxTime:
#             return 'No'
#         while currentMoves > 0:
#             print(visited)
#             pos = queue.pop(0)
#             row, col = pos
#             if row == height-1 and col == width-1 and count <= maxTime:
#                 return 'Yes'
#             visited[row][col] = True
#             for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
#                 newX = x + row
#                 newY = y + col
#                 if newX >= 0 and newX < height and newY >= 0 and newY < width and \
#                         grid[newX][newY] == "." and visited[newX][newY] == False:
#                     queue.append([newX,newY])
#             currentMoves -= 1
#         count += 1

#     return 'No'
