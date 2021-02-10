class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 1
        node = head
        while node.next is not None:
            node = node.next
            count += 1

        if count == n:
            return head.next

        steps = count - n - 1
        node = head
        while steps > 0:
            node = node.next
            steps -= 1

        node.next = node.next.next
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        i = head
        j = head
        steps = n
        while steps > 0:
            j = j.next
            steps -= 1

        if j is None: #i is head, remove head
            return head.next

        while j.next is not None:
            j = j.next
            i = i.next

        i.next = i.next.next
        return head
