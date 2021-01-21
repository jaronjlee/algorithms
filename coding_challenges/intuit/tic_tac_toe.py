import collections


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [["_"] * n for _ in range(n)]
        self.n = n
        self.Xrows = collections.defaultdict(int)
        self.Xcols = collections.defaultdict(int)
        self.Orows = collections.defaultdict(int)
        self.Ocols = collections.defaultdict(int)
        self.Ldiag = collections.defaultdict(int)
        self.Rdiag = collections.defaultdict(int)

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        if player == 1:
            self.board[row][col] = "X"
            self.Xrows[row] += 1
            self.Xcols[col] += 1
            if self.Xrows[row] == self.n or self.Xcols[col] == self.n:
                return 1
        elif player == 2:
            self.board[row][col] = "O"
            self.Orows[row] += 1
            self.Ocols[col] += 1
            if self.Orows[row] == self.n or self.Ocols[col] == self.n:
                return 2

        if row == col:
            self.Ldiag[player] += 1
            if self.Ldiag[player] == self.n:
                return player

        if row + col == self.n-1:
            self.Rdiag[player] += 1
            if self.Rdiag[player] == self.n:
                return player

        return 0


# class TicTacToe:

#     def __init__(self, n: int):
#         """
#         Initialize your data structure here.
#         """
#         self.n = n
#         self.rows = [0]*n
#         self.cols = [0]*n
#         self.Ldiag = 0
#         self.Rdiag = 0

#     def move(self, row: int, col: int, player: int) -> int:
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         """
#         add = 0
#         if player == 1:
#             add = 1
#         else:
#             add = -1

#         self.rows[row] += add
#         self.cols[col] += add

#         if row == col:
#             self.Ldiag += add
#         if row + col == self.n-1:
#             self.Rdiag += add

#         if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.Ldiag) == self.n or abs(self.Rdiag) == self.n:
#             return player

#         return 0
