__author__ = 'Adward'
import collections

class TicTacToe2(object):
    def __init__(self, n):
        count = collections.Counter()

        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0

        self.move = move

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.rev_diag = 0


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        p = 1 if player == 1 else -1
        self.rows[row] += p
        self.cols[col] += p

        if row == col:   # on diagonal
            self.diag += p
            if abs(self.diag) == self.n:
                return 1 if self.diag > 0 else 2
        if row+col == self.n-1:
            self.rev_diag += p
            if abs(self.rev_diag) == self.n:
                return 1 if self.rev_diag > 0 else 2

        if abs(self.rows[row]) == self.n:
            return 1 if self.rows[row] > 0 else 2
        if abs(self.cols[col]) == self.n:
            return 1 if self.cols[col] > 0 else 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)