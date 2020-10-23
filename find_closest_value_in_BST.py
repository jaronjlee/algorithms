def findClosestValueInBst(tree, target):
    # Write your code here.
    closest = tree.value
	current_node = tree
	
	while current_node is not None:
		best_diff = abs(target - closest)
		if abs(target - current_node.value) < best_diff:
			closest = current_node.value
		
		if target > current_node.value:
			current_node = current_node.right
		else:
			current_node = current_node.left
			
			
	return closest