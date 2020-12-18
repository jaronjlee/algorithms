class Solution:
    def floodFill(self, image, sr, sc, newColor):
        startColor = image[sr][sc]
        if startColor == newColor:
            return image
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        imageHeight = len(image)
        imageWidth = len(image[0])
        queue = deque([(sr, sc)])
        while queue:
            position = queue.popleft()
            positionR = position[0]
            positionC = position[1]
            if image[positionR][positionC] == startColor:
                image[positionR][positionC] = newColor
                for direction in directions:
                    newR = position[0] + direction[0]
                    newC = position[1] + direction[1]
                    if newR in range(imageHeight) and newC in range(imageWidth):
                        queue.append((newR, newC))
        return image
# class Solution:
#     def floodFill(self, image, sr, sc, newColor):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type newColor: int
#         :rtype: List[List[int]]
#         """
#         def findConnectedPixels(position, image):
#                 imageHeight = len(image)
#                 imageWidth = len(image[0])
#                 directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
#                 newPositions = []
#                 for direction in directions:
#                     newR = position[0] + direction[0]
#                     newC = position[1] + direction[1]
#                     if newR in range(imageHeight) and newC in range(imageWidth):
#                         newPositions.append([newR, newC])
#                 return newPositions
#         startColor = image[sr][sc]
#         if startColor == newColor:
#             return image
#         queue = deque([[sr,sc]])
#         while queue:
#             position = queue.popleft()
#             positionR = position[0]
#             positionC = position[1]
#             if image[positionR][positionC] == startColor:
#                 image[positionR][positionC] = newColor
#                 newPositions = findConnectedPixels(position, image)
#                 queue += newPositions
#         return image
