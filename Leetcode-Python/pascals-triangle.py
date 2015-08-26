__author__ = 'Adward'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []

        triangle = [[1]]
        row = 2
        while row <= numRows:
            newRow = [1]
            for i in range(row-2):
                tmp1 = triangle[row-2][i]
                tmp2 = triangle[row-2][i+1]
                newRow.append(tmp1+tmp2)
            newRow.append(1)
            triangle.append(newRow)
            row += 1
        return triangle

sol = Solution()
print(sol.generate(2))

