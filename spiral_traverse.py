def spiralTraverse(array):
    # Write your code here.
    result = []
	
	SR = 0
	ER = len(array)-1
	SC = 0
	EC = len(array[0])-1
	
	while SR <= ER and SC <= EC:
		
		#top left to top right
		for col in range(SC, EC+1):
			result.append(array[SR][col])
		
		#top right to bottom right
		for row in range(SR+1, ER+1):
			result.append(array[row][EC])
		
		#bottom right to bottom left
		for col in range(EC-1, SC-1, -1):
			if SR == ER:
				break
			result.append(array[ER][col])
			
		#bottom left to top left
		for row in range(ER-1, SR, -1):
			if SC == EC:
				break
			result.append(array[row][SC])
		
		SR += 1
		ER -= 1
		SC += 1
		EC -= 1
	
	return result