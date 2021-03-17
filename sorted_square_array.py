def sortedSquaredArray(array):
    left = 0


right = len(array)-1
result = []

while left <= right:
		leftNum = array[left]
		rightNum = array[right]
		if abs(leftNum) > abs(rightNum):
			result.insert(0, leftNum**2)
			left += 1
		else:
			result.insert(0, rightNum**2)
			right -= 1

	return result
