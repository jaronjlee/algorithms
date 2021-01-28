# prerequisites = [[4, 3], [3, 2], [2, 1]]
# numCourses = 4

# 1 -> 2 -> 3 -> 4

# indegree = {
#     4: 3,
#     3: 2,
#     2: 1
# }
# outdegree = {
#     3: 4,
#     2: 3,
#     1: 2
# }

# count = 0
# stack = [1]  # nodes in stack without edges going into them are the starting nodes

# #pop off nodes
# stack = [1] = > []
# count = 1
# node = 1
# for n in outdegree[1]:  # 1:2
#     indegree[2].remove(1)


# 2 -> 3 -> 4

# indegree = {
#     4: 3,
#     3: 2,
#     2: None
# }
# outdegree = {
#     3: 4,
#     2: 3,
#     1: 2
# }


# #pop off nodes
# stack = [2] = > []
# count = 2
# node = 2
# for n in outdegree[2]:
#     indegree[3].remove(2)


# 2 -> 3 -> 4

# indegree = {
#     4: 3,
#     3: 2,
#     2: None
# }
# outdegree = {
#     3: 4,
#     2: 3,
#     1: 2
# }


#topological sort
#create indegree and outdegree hashes
#find nodes without nodes coming in, and start removing them from indegree and keep a count


# indegree = {
#     4:3,
#     3:2,
#     2:1
# }

# outdegree = {
#     1:2,
#     2:3,
#     3:4
# }


from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = defaultdict(set)
        outdegree = defaultdict(set)

        for course, pre in prerequisites:
            indegree[course].add(pre)
            outdegree[pre].add(course)

        stack = []
        count = 0

        for course in range(numCourses):
            if course not in indegree:
                stack.append(course)

        print(stack)

        while stack:
            node = stack.pop()
            count += 1
            nextNodes = outdegree[node]
            for nextNode in nextNodes:
                indegree[nextNode].remove(node)
                if not indegree[nextNode]:
                    stack.append(nextNode)

        return count == numCourses
