def mergeSort(array):
    if len(array) <= 1:
		return array

	midIdx = len(array) // 2
	left = array[0:midIdx]
	right = array[midIdx:]
	sortedLeft = mergeSort(left)
	sortedRight = mergeSort(right)
	return mergeSortedArrays(sortedLeft, sortedRight)

def mergeSortedArrays(left, right):
	result = []
	
	while left and right:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
			
	result = result + left + right
	return result
