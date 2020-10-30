def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
	arrayTwo.sort()
	
	
	smallest = None
	result = []
	
	for num1 in arrayOne:
		for num2 in arrayTwo:
			diff = None
			if num1 > num2:
				diff = num1 - num2
			else:
				diff = num2 - num1
			
			if smallest is None or diff < smallest:
				smallest = diff
				result = [num1, num2]
	
	return result


def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
	arrayTwo.sort()
	
	i = 0
	j = 0
	smallest = float("inf")
	result = []
	
	while i < len(arrayOne) and j < len(arrayTwo):
		num1 = arrayOne[i]
		num2 = arrayTwo[j]
		diff = None
		if num1 >= num2:
			diff = num1 - num2
			j += 1
		else:
			diff = num2 - num1
			i += 1
		
		if diff < smallest:
			smallest = diff
			result = [num1, num2]
			
	return result