# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = findDepth(topAncestor, descendantOne)
    depthTwo = findDepth(topAncestor, descendantTwo)


diff = None
deepestNode = None
otherNode = None

if depthTwo > depthOne:
		diff = depthTwo - depthOne
		deepestNode = descendantTwo
		otherNode = descendantOne
	else:
		diff = depthOne - depthTwo
		deepestNode = descendantOne
		otherNode = descendantTwo

	while diff > 0:
		deepestNode = deepestNode.ancestor
		diff -= 1

	while deepestNode != otherNode:
		deepestNode = deepestNode.ancestor
		otherNode = otherNode.ancestor

	return deepestNode


def findDepth(topAncestor, descendant):
	depth = 0
	currentNode = descendant

	while currentNode != topAncestor:
		currentNode = currentNode.ancestor
		depth += 1

	return depth


#OR-----------------------------------------------------

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        queue = [root]
        
        #fill up parent dictionary
        while p not in parent or q not in parent:
            currentNode = queue.pop(0)
            if currentNode.left:
                parent[currentNode.left] = currentNode
                queue.append(currentNode.left)
            if currentNode.right:
                parent[currentNode.right] = currentNode
                queue.append(currentNode.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
            
        print(ancestors)
        return q


#OR-------------------------------------------------------
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findDepth(root, node, parentTree):
            depth = 0
            while root != node:
                node = parentTree[node]
                depth += 1
            return depth
    
        parent = {root: None}
        queue = [root]
        
        #fill up parent dictionary
        while p not in parent or q not in parent:
            currentNode = queue.pop(0)
            if currentNode.left:
                parent[currentNode.left] = currentNode
                queue.append(currentNode.left)
            if currentNode.right:
                parent[currentNode.right] = currentNode
                queue.append(currentNode.right)
                
        depthOne = findDepth(root, p, parent)
        depthTwo = findDepth(root, q, parent)
        diff = None
        deeperNode = None
        otherNode = None
        
        if depthTwo > depthOne:
            deeperNode = q
            otherNode = p
            diff = depthTwo - depthOne
        else:
            deeperNode = p
            otherNode = q
            diff = depthOne - depthTwo
            
        while diff > 0:
            deeperNode = parent[deeperNode]
            diff -= 1
            
        while deeperNode != otherNode:
            deeperNode = parent[deeperNode]
            otherNode = parent[otherNode]
            
        return deeperNode
