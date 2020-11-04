def isMonotonic(array):
    # Write your code here.
    if len(array) < 2:
		return True
	
	increasing = False
	decreasing = False
	
	for i in range(0, len(array)-1):
		first = array[i]
		second = array[i+1]
		if second - first == 0:
			continue
		elif second - first > 0:
			increasing = True
		elif second - first < 0:
			decreasing = True
		
		if increasing is True and decreasing is True:
			return False
	
	return True
	