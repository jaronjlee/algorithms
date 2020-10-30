def nodeDepths(root):
    # Write your code here.
    running_sum = 0
	stack = [{"node": root, "depth":0}]

	while len(stack) > 0:
		node_info = stack.pop()
		node = node_info["node"]
		depth = node_info["depth"]
		if node is None:
			continue
		running_sum += depth
		stack.append({"node": node.left, "depth": depth+1})
		stack.append({"node": node.right, "depth": depth+1})
		
	return running_sum

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None