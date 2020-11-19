def kadanesAlgorithm(array):
    # Write your code here.
	max_sums = [0]*len(array)
	max_sums[0] = array[0]
	print(array)
	print(max_sums)
	
	current_max = max_sums[0]
    for i in range(1, len(array)):
		new_sum = array[i] + max_sums[i-1]
		max_sums[i] = max(array[i], new_sum)
		if max_sums[i] > current_max:
			current_max = max_sums[i]
			
		
	return current_max