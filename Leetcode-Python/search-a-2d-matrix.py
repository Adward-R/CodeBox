__author__ = 'Adward'
import bisect
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            y = bisect.bisect_right([line[0] for line in matrix], target) - 1
        except:
            return False
        if y < 0:
            return False
        x = bisect.bisect_left(matrix[y], target)

        if x >= len(matrix[y]) or matrix[y][x] != target:
            return False
        else:
            return True

sol = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
#print(sol.searchMatrix(matrix, 100))
print(sol.searchMatrix([[1,2,5]],3))