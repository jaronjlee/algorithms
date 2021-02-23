#minHeap: every parent node must be smaller than its children
#peek: look at the root node (smallest)
#remove: remove the root node, swap root and last node, then sift root node down
#add: add node to end of the array, sift up until it cannot anymore
#build: start at last parent node and sift all nodes down

 #       1
 #    3     2
 #  7  4   3  6
 # 9  8

# [1, 3, 2, 7, 4, 3, 6, 9, 8]


# currentNode = i
# childOne = (i * 2) + 1
# childTwo = (i * 2) + 2
# parentNode = (i - 1) // 2


class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        lastParentIdx = ((len(array)-1) - 1) // 2
	for i in reversed(range(0, lastParentIdx + 1)):
			self.siftDown(i, len(array)-1, array)
		return array

    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
	while childOneIdx <= endIdx:
			childTwoIdx = currentIdx * 2 + 2
			idxToSwap = None
			if childTwoIdx <= endIdx and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
			if heap[idxToSwap] < heap[currentIdx]:
				heap[currentIdx], heap[idxToSwap] = heap[idxToSwap], heap[currentIdx]
				currentIdx = idxToSwap
				childOneIdx = currentIdx * 2 + 1
			else:
				break

    def siftUp(self, currentIdx, heap):
        while currentIdx > 0:
			parentIdx = (currentIdx - 1) // 2
			if heap[currentIdx] < heap[parentIdx]:
				heap[currentIdx], heap[parentIdx] = heap[parentIdx], heap[currentIdx]
				currentIdx = parentIdx
			else:
				break

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
	removedEle = self.heap.pop()
		self.siftDown(0, len(self.heap)-1, self.heap)
		return removedEle

    def insert(self, value):
        self.heap.append(value)
	self.siftUp(len(self.heap)-1, self.heap)
