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

sol = Solution()
print(sol.uniquePaths(3,3))