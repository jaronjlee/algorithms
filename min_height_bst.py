def minHeightBst(array):
    return constructBst(array, None, 0, len(array)-1)


def constructBst(array, bst, start, end):
	if start > end:
		return
	mid = (start + end) // 2
	midValue = array[mid]
	if bst is None:
		bst = BST(midValue)
	else:
		bst.insert(midValue)
	constructBst(array, bst, start, mid-1)
	constructBst(array, bst, mid+1, end)
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
