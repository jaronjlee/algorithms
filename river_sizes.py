def riverSizes(matrix):
    height = len(matrix)


width = len(matrix[0])
result = []


def bfs(row, col, height, width, size):
		queue = [[row, col]]
		while queue:
			pos = queue.pop(0)
			size += 1
			for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				newX = pos[0] + x
				newY = pos[1] + y
				if newX >= 0 and newX < height and newY >= 0 and newY < width and \
                                        matrix[newX][newY] == 1:
					matrix[newX][newY] = 0
					queue.append([newX, newY])

		return size

	for row in range(height):
		for col in range(width):
			if matrix[row][col] == 1:
				matrix[row][col] = 0
				result.append(bfs(row, col, height, width, 0))

	return result
