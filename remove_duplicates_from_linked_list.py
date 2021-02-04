#                                 C     N
# 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> None

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList


while currentNode is not None:
		nextDistinct = currentNode.next
		while nextDistinct is not None and nextDistinct.value == currentNode.value:
			nextDistinct = nextDistinct.next

		currentNode.next = nextDistinct
		currentNode = nextDistinct

	return linkedList
