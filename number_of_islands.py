class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  # m X n

      count = 0

      n = len(grid)
      m = len(grid[0])

      def bfs_islands(mat, i, j):
        # mark as visited
        mat[i][j] = 0

        # can i look left?
        if i - 1 >= 0 and mat[i-1][j] == "1":
          bfs_islands(mat, i-1, j)

        # can i look right?
        if i + 1 < n and mat[i+1][j] == "1":
          bfs_islands(mat, i+1, j)

        # can i look down?
        if j - 1 >= 0 and mat[i][j-1] == "1":
          bfs_islands(mat, i, j-1)

        # can i look down?
        if j + 1 < m and mat[i][j+1] == "1":
          bfs_islands(mat, i, j+1)

      for i in range(n):
        for j in range(m):

          if grid[i][j] == "1":

            # once we hit "1", we "clean" all it's "real-estate" with BFS
            count += 1
            bfs_islands(grid, i, j)

      return count
