def invertBinaryTree(tree):
    queue = [tree]


while queue:
		node = queue.pop(0)
		if node is None:
			continue
		node.left, node.right = node.right, node.left
		queue.append(node.left)
		queue.append(node.right)

	return tree
