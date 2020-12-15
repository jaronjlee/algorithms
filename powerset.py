def powerset(array):
	if len(array) < 1:
		return [[]]

	lastIdx = len(array)-1
	lastEle = array[lastIdx]
	subsets = powerset(array[0:lastIdx])

	for i in range(0, len(subsets)):
		subsets.append(subsets[i] + [lastEle])

	return subsets  # =>  [[], [1]]


def powerset(array):
    if len(array) < 1:
		return [[]]

	prevArr = powerset(array[0:len(array)-1])
	i = 0
	cap = len(prevArr)
	
	while i < cap:
		prevArr.append(prevArr[i] + [array[-1]])
		i += 1
		
	return prevArr
