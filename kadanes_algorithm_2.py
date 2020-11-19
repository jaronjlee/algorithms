def kadanesAlgorithm(array):
    # Write your code here.
	max_ending = array[0]
	result = array[0]
	
    for i in range(1, len(array)):
		num = array[i]
		max_ending = max(num, num + max_ending)
		result = max(max_ending, result)
		
	return result