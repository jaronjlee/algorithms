def binarySearch(array, target):
    # Write your code here.
	return bSearchHelper(array, target, 0, len(array)-1)
	
	
def bSearchHelper(array, target, left, right):
	while left <= right:
		midIdx = (right+left)//2
		midEle = array[midIdx]

		if target == midEle:
			return midIdx
		elif target < midEle:
			right = midIdx - 1
		else:
			left = midIdx + 1

	return -1