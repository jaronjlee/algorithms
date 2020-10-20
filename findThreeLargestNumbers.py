def findThreeLargestNumbers(array):
    # Write your code here.
    initial = [array[0], array[1], array[2]]
	result = sorted(initial)
	
	for ele in array[3:]:
		if ele > result[2]:
			result[0] = result[1]
			result[1] = result[2]
			result[2] = ele
		elif ele < result[2] and ele > result[1]:
			result[0] = result[1]
			result[1] = ele
		elif ele < result[1] and ele > result[0]:
			result[0] = ele
			
	return result