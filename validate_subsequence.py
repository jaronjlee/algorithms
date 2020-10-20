def isValidSubsequence(array, sequence):
    # Write your code here.

	j = 0
	for i in range(len(array)):
		if array[i] == sequence[j]:
			j += 1
		
		if j == len(sequence):
			return True
		
	return False