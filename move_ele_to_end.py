def moveElementToEnd(array, toMove):
    # Write your code here.
    
	i = 0
	j = len(array)-1
	
	while j > i:
		if array[j] == toMove:
			j -= 1
		elif array[i] != toMove:
			i += 1
		
		if array[i] == toMove and array[j] != toMove:
			array[i], array[j] = array[j], array[i]
			i += 1
			j -= 1
	
	return array