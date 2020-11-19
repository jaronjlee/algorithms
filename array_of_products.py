def arrayOfProducts(array):
    # Write your code here.
    left = [array[0]]
	right = [array[-1]]
	result = []
	
	for i in range(1, len(array)):
		left.append(left[i-1]*array[i])
		
	for i in range(len(array)-2, -1, -1):
		print(i)
		print(len(array)-2-i)
		right.append(right[len(array)-2-i]*array[i])
		
	for i in range(0, len(array)):
		leftIdx = i - 1
		rightIdx = len(array)-1 - (i + 1)
		
		if leftIdx < 0:
			result.append(right[rightIdx])
		elif rightIdx < 0:
			result.append(left[leftIdx])
		else:
			result.append(right[rightIdx]*left[leftIdx])
			
	return result