from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for origin, destination in tickets:
            adj[origin].append(destination)

        for origin in adj:
            adj[origin].sort(reverse=True)

        stack = ["JFK"]
        result = []

        while stack:
            airport = stack[-1]
            if airport in adj and len(adj[airport]) > 0:
                stack.append(adj[airport].pop())
            else:
                result.append(stack.pop())

        return result[::-1]
