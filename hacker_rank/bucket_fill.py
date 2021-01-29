
def strokesRequired(picture):
    visited = [[False]*len(picture[0]) for _ in range(len(picture))]
    count = 0
    height = len(picture)
    width = len(picture[0])

    def bfs(visited, row, col, letter, height, width):
        queue = [[row, col]]
        while queue:
            currentSquare = queue.pop(0)
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newRow = currentSquare[0] + x
                newCol = currentSquare[1] + y
                if newRow >= 0 and newRow < height and newCol >= 0 and newCol < width and \
                        picture[newRow][newCol] == letter and visited[newRow][newCol] == False:
                    visited[newRow][newCol] = True
                    queue.append([newRow, newCol])

        return True

    for row in range(height):
        for col in range(width):
            if visited[row][col] == False:
                visited[row][col] = True
                count += 1
                bfs(visited, row, col, picture[row][col], height, width)

    return count
