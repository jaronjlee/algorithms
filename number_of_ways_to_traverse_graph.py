def numberOfWaysToTraverseGraph(width, height):
    dp = [[None] * width for _ in range(0, height)]


for row in range(0, height):
		dp[row][0] = 1

	for col in range(0, width):
		dp[0][col] = 1

	for row in range(1, height):
		for col in range(1, width):
			dp[row][col] = dp[row][col-1] + dp[row-1][col]

	return dp[-1][-1]
