def hasSingleCycle(array):
    # Write your code here.
	count = 0
	i = 0
	while count < len(array):
		if count > 0 and i == 0:
			return False
		count += 1
		jump = array[i]
		next_idx = (i + jump) % len(array)
		i = next_idx
	return i == 0