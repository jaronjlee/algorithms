# ‘ABBCCCBA’ -> ‘AA’
# ‘ABBCCCBAA’ -> ‘’
# ‘ABBCCCBCA’ -> ‘ACA’
# ‘ABBCCCBBCA’ -> ‘ACA’

# SO IF THERE ARE 3 OR MORE RECURRING CHARCTERS THEY ARE TO BE REMOVED
# THE WORST POSSIBLE TIME COMPLEXITY YOU ARE ALLOWED IS O(n)

#use stack to store output chars
#iterate through input string once
#append chars to the stack


def collapseString(str):
	if len(str) < 3:
		return str

	stack = []
	stack.append(str[0])
	stack.append(str[1])

	i = 2


while i < len(str):
	if len(stack) < 2:
		stack.append(str[i])
		i += 1
	elif stack[-1] != stack[-2] or stack[-1] == stack[-2] and str[i] != stack[-1]:
		stack.append(str[i])
		i += 1
elif stack[-1] == stack[-2] and str[i] == stack[-1]
last = stack.pop()
secondLast = stack.pop()
while str[i] == last:
	i += 1

return “”.join(stack)
