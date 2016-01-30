__author__ = 'Adward'
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        try:
            n = len(grid[0])
            if n == 0:
                return 0
        except:
            return 0

        for j in range(1, m):
            grid[j][0] += grid[j-1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

sol = Solution()
grid = [
    [1,2,4,1],
    [3,4,2,2],
    [2,1,1,3],
    [3,2,5,2]
]
print(sol.minPathSum(grid))