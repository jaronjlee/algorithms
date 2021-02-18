def nonConstructibleChange(coins):
    if len(coins) == 0:
		return 1

	coins.sort()
	maxChange = coins[0]
	
	if maxChange > 1:
		return 1
	
	for coin in coins[1:]:
		if coin > maxChange + 1:
			return maxChange + 1
		elif coin <= maxChange + 1:
			maxChange += coin
		
	return maxChange + 1
		
