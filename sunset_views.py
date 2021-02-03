
def sunsetViews(buildings, direction):
	if not buildings:
		return []

	dp = [0] * len(buildings)
	result = []

    curr = None
	increment = None
	if direction == "WEST":
		curr = 1
		increment = 1
	else:
		curr = len(buildings)-2
		increment = -1
		
	result.append(curr-increment)
		
	while 0 <= curr < len(buildings):
		dp[curr] = max(buildings[curr-increment], dp[curr-increment])
		if buildings[curr] > dp[curr]:
			result.append(curr)
		curr += increment
	
	if direction == "EAST":
		return result[::-1]

	return result
