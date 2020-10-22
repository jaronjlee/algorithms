def balancedBrackets(string):
    # Write your code here.
    if len(string) < 2:
		return false
	
	open_brackets = ["(", "[", "{"]
	close_brackets = [")", "]", "}"]
	
	if string[0] in close_brackets:
		return False
	
	stack = [string[0]]
	
	for i in range(1, len(string)):
		if string[i] in open_brackets:
			stack.append(string[i])
		
		if string[i] in close_brackets:
			last_open_idx = open_brackets.index(stack[-1])
			next_close_idx = close_brackets.index(string[i])
			if last_open_idx == next_close_idx:
				stack.pop(-1)
			else:
				return False

	if len(stack) == 0:
		return True
	else:
		return False
				
		