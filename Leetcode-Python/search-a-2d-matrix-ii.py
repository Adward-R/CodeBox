__author__ = 'Adward'

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return False

        yUpperBound = m - 1
        while yUpperBound > 0 and matrix[yUpperBound][0] > target:
            yUpperBound -= 1
        yUpperBound += 1

        yLowerBound = 0
        while yLowerBound < m and matrix[yLowerBound][n-1] < target:
            yLowerBound += 1

        xUpperBound = n - 1
        while xUpperBound > 0 and matrix[0][xUpperBound] > target:
            xUpperBound -= 1
        xUpperBound += 1

        xLowerBound = 0
        while xLowerBound < n and matrix[m-1][xLowerBound] < target:
            xLowerBound += 1

        mat = [row[xLowerBound:xUpperBound] for row in matrix[yLowerBound:yUpperBound]]
        mm = yUpperBound - yLowerBound
        nn = xUpperBound - xLowerBound
        if mm == 0 or nn == 0:
            return False

        '''
        print(yLowerBound)
        print(yUpperBound)
        print(xLowerBound)
        print(xUpperBound)
        print(mat)
        '''

        for row in mat:
            left = 0
            right = nn - 1
            while right - left > 1:
                mid = int((left+right)/2)
                if row[mid] > target:
                    right = mid
                elif row[mid] < target:
                    left = mid
                else:
                    return True
            if row[left] == target or row[right] == target:
                return True
        return False

sol = Solution()
'''
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''
matrix = [[-1, 3]]
print(sol.searchMatrix(matrix, 1))