__author__ = 'Adward'
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk1 = []
        self.stk2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stk1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.stk1) > 0:
            tmp = self.stk1[-1]
            self.stk1.pop()
            self.stk2.append(tmp)
        res = self.stk2[-1]
        self.stk2.pop()
        while len(self.stk2) > 0:
            tmp = self.stk2[-1]
            self.stk2.pop()
            self.stk1.append(tmp)
        return res

    def peek(self):
        """
        :rtype: int
        """
        while len(self.stk1) > 0:
            tmp = self.stk1[-1]
            self.stk1.pop()
            self.stk2.append(tmp)
        res = self.stk2[-1]
        while len(self.stk2) > 0:
            tmp = self.stk2[-1]
            self.stk2.pop()
            self.stk1.append(tmp)
        return res

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stk1) == 0

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.pop()
print(q.peek())
q.push(5)
print(q.peek())
print(q.empty())