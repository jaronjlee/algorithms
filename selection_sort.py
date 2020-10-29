def selectionSort(array):
    # Write your code here.
    for i in range(0, len(array)):
		smallest = i
		j = i
		while j < len(array):
			if array[j] < array[smallest]:
				smallest = j
			j += 1
		
		array[i], array[smallest] = array[smallest], array[i]
	
	return array
		
		
