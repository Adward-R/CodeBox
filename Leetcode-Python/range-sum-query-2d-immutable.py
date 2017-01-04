__author__ = 'Adward'
class NumMatrix(object):
    def __init__(self, matrix):
        try:
            self.m, self.n = len(matrix), len(matrix[0])
        except:
            self.m, self.n = 0, 0
            return
        self.DP = []
        for i in range(self.m):
            curRowSum = 0
            row = []
            for j in range(self.n):
                curRowSum += matrix[i][j]
                row.append(curRowSum + (self.DP[i-1][j] if i else 0))
            self.DP.append(row)

    def sumRegion(self, row1, col1, row2, col2):
        if self.m == 0:
            return 0
        row2, col2 = min(row2, self.m-1), min(col2, self.n-1)
        area = self.DP[row2][col2]
        if row1 > 0:
            area -= self.DP[row1-1][col2]
            if col1 > 0:
                area += self.DP[row1-1][col1-1]
        if col1 > 0:
            area -= self.DP[row2][col1-1]
        return area

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sol = NumMatrix(matrix)
print(sol.sumRegion(-1,-2,2,4))
