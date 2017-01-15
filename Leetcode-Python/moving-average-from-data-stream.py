__author__ = 'Adward'
from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sz = size
        self.dq = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.dq.append(val)
        self.sum += val
        if len(self.dq) > self.sz:
            self.sum -= self.dq.popleft()
        return self.sum * 1.0 / len(self.dq)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)