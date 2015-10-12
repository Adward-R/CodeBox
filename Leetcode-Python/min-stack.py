__author__ = 'Adward'
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk = []
        self.minstk = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stk.append(x)
        if len(self.minstk) == 0 or x <= self.minstk[-1]:
            self.minstk.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.stk[-1] == self.minstk[-1]:
            self.minstk.pop()
        self.stk.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstk[-1]
