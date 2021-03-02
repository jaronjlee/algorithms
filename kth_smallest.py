class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.found = False
        self.helper(root)
        return self.res

    def helper(self, node):
        #exit as soon as possible
        if self.found:
            return
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            self.found = True
            return
        self.helper(node.right)
