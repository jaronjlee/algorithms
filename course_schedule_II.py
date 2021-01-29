from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        indegree = defaultdict(set)
        outdegree = defaultdict(set)

        for course, pre in prerequisites:
            outdegree[pre].add(course)
            indegree[course].add(pre)

        queue = []

        for course in range(0, numCourses):
            if course not in indegree:
                queue.append(course)

        while queue:
            currentNode = queue.pop(0)
            if currentNode in outdegree:
                for nextNode in outdegree[currentNode]:
                    indegree[nextNode].remove(currentNode)
                    if not indegree[nextNode]:
                        queue.append(nextNode)
            result.append(currentNode)

        if numCourses == len(result):
            return result
        else:
            return []
