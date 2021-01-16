def largestSubgrid(grid, maxSum):

    height = len(grid)
    width = len(grid[0])

    sum = [[0 for i in range(width + 1)] for j in range(n + 1)]

    for i in range(n + 1):

        for j in range(width+1):
            if (i == 0 or j == 0):
                sum[i][j] = 0
                continue

            sum[i][j] = grid[i - 1][j - 1] + sum[i - 1][j] + \
                sum[i][j - 1]-sum[i - 1][j - 1]

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if (i + ans - 1 > n or j + ans - 1 > width):
                break

            mid = ans
            lo = ans

            hi = min(n - i + 1, width - j + 1)

            # Binary Search
            while (lo < hi):
                mid = (hi + lo + 1) // 2

                if (sum[i + mid - 1][j + mid - 1] +
                    sum[i - 1][j - 1] -
                    sum[i + mid - 1][j - 1] -
                        sum[i - 1][j + mid - 1] <= maxSum):
                    lo = mid
                else:
                    hi = mid - 1
            ans = max(ans, lo)
            
    print(ans - 1)
