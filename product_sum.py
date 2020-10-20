def productSum(array, level = 1):
    result = 0
	
	for ele in array:
		if type(ele) == int:
			result += ele
		elif type(ele) == list:
			result += productSum(ele, level+1)
			
			
	return level * result
