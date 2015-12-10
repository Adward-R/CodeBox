__author__ = 'Adward'
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rowNum = len(board)
        if rowNum == 0:
            return
        colNum = len(board[0])
        if colNum == 0:
            return

        for i in range(rowNum):
            for j in range(colNum):
                srdLives = 0
                for k in range(max(0, i-1), min(rowNum, i+2)):
                    for l in range(max(0, j-1), min(colNum, j+2)):
                        tmp = board[k][l]
                        if tmp < 0:
                            tmp = - tmp - 1
                        srdLives += tmp
                srdLives -= board[i][j]
                if board[i][j]: #living
                    if srdLives < 2 or srdLives > 3: #to die
                        board[i][j] = -2
                else: #dead
                    if srdLives == 3: #to live again
                        board[i][j] = -1

        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] < 0:
                    board[i][j] = int(not (-board[i][j] - 1))

sol = Solution()
board = [
    [1, 0, 1],
    [1, 1, 1],
    [0, 0, 1]
]
sol.gameOfLife(board)
print(board)