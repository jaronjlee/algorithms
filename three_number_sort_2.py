def threeNumberSort(array, order):
    # Write your code here.
	leftEle = order[0]
	middleEle = order[1]
	rightEle = order[2]
	
	countLeftEle = 0
	countMiddleEle = 0
	countRightEle = 0
	
	for num in array:
		if num == leftEle:
			countLeftEle += 1
		elif num == middleEle:
			countMiddleEle += 1
		else:
			countRightEle += 1
			
	countMiddleEle += countLeftEle
	countRightEle += countMiddleEle
	
	for i in range(0, len(array)):
		if i in range(0, countLeftEle):
			array[i] = leftEle
		elif i in range(countLeftEle, countMiddleEle):
			array[i] = middleEle
		elif i in range(countMiddleEle, countRightEle):
			array[i] = rightEle
		
			
	return array