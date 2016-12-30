__author__ = 'Adward'
from collections import deque
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = food
        self.isSnake = {(0, 0)}
        self.body = deque([(0, 0)])
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        w, h = self.width, self.height
        fi, fj = self.food[self.score] if self.score < len(self.food) else (-1, -1)
        si, sj = self.body[0]
        if direction == 'U' and si > 0:
            si -= 1
        elif direction == 'L' and sj > 0:
            sj -= 1
        elif direction == 'R' and sj < w - 1:
            sj += 1
        elif direction == 'D' and si < h - 1:
            si += 1
        else:
            return -1  # game over by colliding a wall
            # raise ValueError('Invalid Directional Param!')

        self.body.appendleft((si, sj))
        if si == fi and sj == fj:
            self.score += 1
        else:
            self.isSnake.remove(self.body.pop())
            if (si, sj) in self.isSnake:
                return -1  # game over by colliding with own body
        self.isSnake.add((si, sj))
        return self.score


# Your SnakeGame object will be instantiated and called as such:
width, height = 4, 3
food = [[0, 2], [0, 3], [1, 3]]
obj = SnakeGame(width, height, food)
directions = ['R', 'R', 'R', 'D', 'L', 'U']
print([obj.move(d) for d in directions])