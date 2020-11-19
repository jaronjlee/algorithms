def runLengthEncoding(string):
    # Write your code here.
    result = ""
	if len(string) == 1:
		return "1" + string[0]
	
	prevEle = string[0]
	countEle = 1
	for i in range(1, len(string)):
		currentEle = string[i]
		if i == len(string)-1:
			if currentEle == prevEle and countEle < 9:
				countEle += 1
				result += str(countEle)
				result += prevEle
				break
			elif currentEle == prevEle and countEle == 9:
				result += str(countEle)
				result += prevEle
				result += "1"
				result += currentEle
			elif currentEle != prevEle:
				result += str(countEle)
				result += prevEle
				result += str(1)
				result += currentEle
				break
		elif currentEle == prevEle and countEle < 9:
			countEle += 1
		elif currentEle == prevEle and countEle == 9:
			result += str(countEle)
			result += prevEle
			countEle = 1
		elif currentEle != prevEle:
			result += str(countEle)
			result += prevEle
			prevEle = currentEle
			countEle = 1

			
	return result