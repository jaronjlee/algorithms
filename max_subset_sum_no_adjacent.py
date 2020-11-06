def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	
	if len(array) < 1:
		return 0
    
	current = array[0]
	previous = None
	
	for i in range(1, len(array)):
		if i == 1:
			previous = current
			if array[i] > previous:
				current = array[i]
			else:
				current = previous
		
		if i > 1:
			if array[i] + previous > current:
				new = array[i] + previous
				previous = current
				current = new
			else:
				previous = current
	
	return current
