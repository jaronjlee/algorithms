def twoNumberSum(array, targetSum):
    # Write your code here.
	d = {}
	
	for num in array:
		diff = targetSum - num
		if diff not in d:
			d[num] = True
		else:
			return [diff, num]
		
	return []
