def threeNumberSum(array, targetSum):
    # Write your code here.
    d = {}
	result = []
	
	for i in range(0, len(array)):
		d[array[i]] = i
		
	for i in range(0, len(array)-1):
		for j in range(i+1, len(array)):
			diff = targetSum - array[i] - array[j]
			# print(diff)
			# print([array[i], array[j], diff])
			if diff in d and diff != array[i] and diff != array[j]:
				sub = [array[i], array[j], diff]
				sub.sort()
				if sub not in result:
					result.append(sub)
	
	# print(result)
	result.sort()
	return result



def threeNumberSum(array, targetSum):
    # Write your code here.
    d = {}
	result = []
	
	for i in range(0, len(array)):
		d[array[i]] = i
		
	for i in range(0, len(array)-1):
		for j in range(i+1, len(array)):
			diff = targetSum - array[i] - array[j]
			# print(diff)
			# print([array[i], array[j], diff])
			if diff in d and diff != array[i] and diff != array[j]:
				sub = [array[i], array[j], diff]
				sub.sort()
				if sub not in result:
					result.append(sub)
	
	# print(result)
	result.sort()
	return result
