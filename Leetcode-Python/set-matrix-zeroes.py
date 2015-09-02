__author__ = 'Adward'
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0

sol = Solution()
'''
matrix = [
    [0,1,1],
    [1,0,1],
    [1,1,1]
]
'''
matrix = [[0,1]]
sol.setZeroes(matrix)
print(matrix)