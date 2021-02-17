def sumOfLinkedLists(linkedListOne, linkedListTwo):
    i = linkedListOne


j = linkedListTwo
currentNode = LinkedList(0)
head = currentNode

carry = 0
while i is not None or j is not None or carry > 0:
		nextDigit = 0
		if i is not None:
			nextDigit += i.value
			i = i.next
		if j is not None:
			nextDigit += j.value
			j = j.next

		nextDigit += carry
		carry = nextDigit // 10
		newVal = nextDigit % 10

		currentNode.value = newVal
		if i is not None or j is not None or carry > 0:
			currentNode.next = LinkedList(0)
		else:
			currentNode.next = None

		currentNode = currentNode.next

	return head
