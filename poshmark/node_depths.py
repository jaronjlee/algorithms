# def nodeDepths(root):
# 	if root is None:
# 		return

# 	runningSum = 0
# 	queue = [{
# 		"node": root,
# 		"depth": 0
# 	}]

# 	while queue:
# 		obj = queue.pop(0)
# 		node = obj["node"]
# 		depth = obj["depth"]

# 		runningSum += depth
# 		if node.left is not None:
# 			leftNode = {
# 				"node": node.left,
# 				"depth": depth + 1
# 			}
# 			queue.append(leftNode)
# 		if node.right is not None:
# 			rightNode = {
# 				"node": node.right,
# 				"depth": depth + 1
# 			}
# 			queue.append(rightNode)

# 	return runningSum

def nodeDepths(root, depth=0):
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return depth

	return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
