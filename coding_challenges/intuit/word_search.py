class Solution:
    def exist(self, board, word) -> bool:
        def dfs(word, row, col, height, width, matchIdx, visited):
            if matchIdx == len(word):
                return True

            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newX = row + rowOffset
                newY = col + colOffset
                if newX >= 0 and newX < height and newY >= 0 and newY < width and \
                        visited[newX][newY] == False and board[newX][newY] == word[matchIdx]:
                    visited[newX][newY] = True
                    if dfs(word, newX, newY, height, width, matchIdx+1, visited):
                        return True
                    visited[newX][newY] = False

            return False

        height = len(board)
        width = len(board[0])
        visited = [[False]*width for _ in range(height)]

        for row in range(height):
            for col in range(width):
                if board[row][col] == word[0]:
                    visited[row][col] = True
                    if dfs(word, row, col, height, width, 1, visited):
                        return True
                    visited[row][col] = False

        return False
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def dfs(word, row, col, height, width, matchIdx, visited):
#             if matchIdx == len(word):
#                 return True

#             for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 newX = row + rowOffset
#                 newY = col + colOffset
#                 if newX >= 0 and newX < height and newY >= 0 and newY < width and \
#                         visited[newX][newY] == False and board[newX][newY] == word[matchIdx]:
#                     visited[newX][newY] = True
#                     if dfs(word, newX, newY, height, width, matchIdx+1, visited):
#                         return True
#                     visited[newX][newY] = False

#             return False

#         height = len(board)
#         width = len(board[0])
#         visited = [[False]*width for _ in range(height)]

#         for row in range(height):
#             for col in range(width):
#                 if board[row][col] == word[0]:
#                     visited[row][col] = True
#                     if dfs(word, row, col, height, width, 1, visited):
#                         return True
#                     visited[row][col] = False

#         return False
