__author__ = 'Adward'
from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0

        grid = [[int(grid[row][col]) for col in range(n)] for row in range(m)]

        gen = 2
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    grid[row][col] = gen
                    dq = deque([(row, col)])
                    while len(dq):
                        i, j = dq.popleft()
                        if i > 0 and grid[i-1][j] == 1:
                            grid[i-1][j] = gen
                            dq.append((i-1, j))
                        if i < m - 1 and grid[i+1][j] == 1:
                            grid[i+1][j] = gen
                            dq.append((i+1, j))
                        if j > 0 and grid[i][j-1] == 1:
                            grid[i][j-1] = gen
                            dq.append((i, j-1))
                        if j < n - 1 and grid[i][j+1] == 1:
                            grid[i][j+1] = gen
                            dq.append((i, j+1))
                    gen += 1
        return gen - 2

sol = Solution()
grid = ["11111011111111101011","01111111111110111110","10111001101111111111","11110111111111111111","10011111111111111111","10111111011101110111","01111111111101101111","11111111111101111011","11111111110111111111","11111111111111111111","01111111011111111111","11111111111111111111","11111111111111111111","11111011111110111111","10111110111011110111","11111111111101111110","11111111111110111100","11111111111111111111","11111111111111111111","11111111111111111111"]
print(sol.numIslands(grid))