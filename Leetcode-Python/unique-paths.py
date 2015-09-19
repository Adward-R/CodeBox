__author__ = 'Adward'

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1
        matrix = []
        for i in range(m):
            matrix.append([1] + [0 for i in range(n-1)])
        for i in range(1, len(matrix[0])):
            matrix[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m <= 0:
            return 0
        n = len((obstacleGrid[0]))
        if n <= 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        matrix = []
        blocked = False
        for i in range(m):
            if blocked:
                matrix.append([0 for k in range(n)])
            else:
                if obstacleGrid[i][0] == 1:
                    matrix.append([0 for k in range(n)])
                    blocked = True
                else:
                    matrix.append([1] + [0 for k in range(n-1)])
        #blocked = False
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                matrix[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

        return matrix[-1][-1]

sol = Solution()
print(sol.uniquePathsWithObstacles([[0,1,0]]))