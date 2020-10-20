def caesarCipherEncryptor(string, key):
    # Write your code here.
    alpha = "abcdefghijklmnopqrstuvwxyz"
	result = []
	# print(alpha)
	
	for i in range(len(string)):
		letter = string[i]
		letter_idx = alpha.index(letter)
		new_idx = (letter_idx + key) % 26
		new_letter = alpha[new_idx]
		result.append(new_letter)
		
	
	return "".join(result)
		
