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

airports = ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

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
