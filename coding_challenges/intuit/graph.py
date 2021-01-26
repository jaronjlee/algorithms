#Given a 2D array, find origin and final destination

# flights = [
#     ["A", "B"],
#     ["A", "C"],
#     ["B", "K"],
#     ["C", "K"],
#     ["E", "L"],
#     ["F", "G"],
#     ["J", "M"],
#     ["E", "F"],
#     ["G", "H"],
#     ["G", "I"],
# ]

# output =
# A: K
# E: H I L
# J: M


#directed graph where nodes have direction
#create adjacency list where key is the departing flight and value is an array of all destinations
#find origin airports
#traverse graph for every origin airport using DFS
#origin airports are airports that do not show up on the right side of the 2D array
#two sets, potential origin airports, destination airports. subtract two sets to come up with origin airports

# adj = {
#     "A": ["B", "C"],
#     "B": ["K"],
#     "C": ["K"],
#     "E": ["L", "F"],
#     "F": ["G"],
#     "G": ["H", "I"],
#     "H": [],
#     "I": [],
#     "J": ["M"],
#     "K": [],
#     "L": [],
#     "M": []
# }

def findDestinations(flights):
    adjList = {}
    potentialOriginAirports = set()
    destinationAirports = set()
    result = {}

    for flight in flights:
        outboundAirport, destinationAirport = flight
        potentialOriginAirports.add(outboundAirport)
        destinationAirports.add(destinationAirport)
        if outboundAirport not in adjList:
            adjList[outboundAirport] = []
        if destinationAirport not in adjList:
            adjList[destinationAirport] = []
        adjList[outboundAirport].append(destinationAirport)

    originAirports = potentialOriginAirports - destinationAirports

    # print(f'adjList = {adjList}')
    # print(f'originAirports = {originAirports}')
    # print(f'destinationAirports = {destinationAirports}')

    for origin in originAirports:
        result[origin] = dfs(adjList, origin, [])

    return result

    
def dfs(adjList, origin, destinations):
    for flight in adjList[origin]:
        if adjList[flight] == [] and flight not in destinations:
            destinations.append(flight)
        dfs(adjList, flight, destinations)

    return destinations


def bfs(origin, adjList, destinations):
  result = []
  queue = adjList[origin]
  while queue:
    flight = queue.pop(0)
    if adjList[flight] != []:
      queue += adjList[flight]
    else:
      if flight not in result:
        result.append(flight)

  return result






flights = [
    ["A", "B"],
    ["A", "C"],
    ["B", "K"],
    ["C", "K"],
    ["E", "L"],
    ["F", "G"],
    ["J", "M"],
    ["E", "F"],
    ["G", "H"],
    ["G", "I"],
]

print(findDestinations(flights))



# def findDestinations(airports, flights, origin):
#     adjList = {}
#     for airport in airports:
#         if airport not in adjList:
#             adjList[airport] = []

#     for k in adjList:
#         for flight in flights:
#             if flight[0] == k:
#                 adjList[k].append(flight[1])

#     print(adjList)
#     return dfs(adjList, origin, [])


# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []

#     def addChild(self, childName):
#         self.children.append(childName)
#         return self

#     def dfs(self, destinations=[]):
#         for child in self.children:
#             if not child.children:
#                 destinations.append(child)
#                 return
#             child.dfs(destinations)

#         return destinations
