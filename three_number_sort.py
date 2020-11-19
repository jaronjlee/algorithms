def threeNumberSort(array, order):
    # Write your code here.
	leftEle = order[0]
	middleEle = order[1]
	rightEle = order[2]
	
	left = []
	middle = []
	right = []
	
	for ele in array:
		if ele == leftEle:
			left.append(ele)
		elif ele == middleEle:
			middle.append(ele)
		else:
			right.append(ele)
			
	return left + middle + right