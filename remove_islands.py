def removeIslands(matrix):
	height = len(matrix)
	width = len(matrix[0])
	land = [[False] * width for _ in range(height)]

	def convertToLand(land, row, col, height, width):
		queue = [[row, col]]

		while queue:
			r, c = queue.pop(0)
			land[r][c] = True
			for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
				newX = r + x
				newY = c + y
				if newX >= 0 and newX < height and newY >= 0 and newY < width and \
                                        land[newX][newY] is False and matrix[newX][newY] == 1:
					queue.append([newX, newY])

	SR = 0
	SC = 0
	ER = len(matrix)
	EC = len(matrix[0])

	#top row
	for col in range(0, EC):
		if matrix[SR][col] == 1:
			convertToLand(land, SR, col, height, width)

	#right col
	for row in range(1, ER):
		if matrix[row][EC-1] == 1:
			convertToLand(land, row, EC-1, height, width)

	#bottom row
	for col in range(EC-2, SC-1, -1):
		if matrix[ER-1][col] == 1:
			convertToLand(land, ER-1, col, height, width)

	for row in range(ER-2, SR, -1):
		if matrix[row][SC] == 1:
			convertToLand(land, row, SC, height, width)

	for row in range(height):
		for col in range(width):
			if matrix[row][col] == 1 and land[row][col] == False:
				matrix[row][col] = 0

	return matrix
