

def isPalindrome(string):
    # Write your code here.
    i = 0
	j = len(string)-1
	
	while j - i >= 1:
		if string[i] is not string[j]:
			return False
		
		i += 1
		j -= 1

	return True