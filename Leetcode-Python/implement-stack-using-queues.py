__author__ = 'Adward'
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)
        for i in range(len(self.q)-1):
            tmp = self.q[0]
            self.q = self.q[1:]
            self.q.append(tmp)

    def pop(self):
        """
        :rtype: nothing
        """
        self.q = self.q[1:]

    def top(self):
        """
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0

stk = Stack()
print(stk.empty())
stk.push(3)
stk.push(2)
stk.push(1)
print(stk.top())
stk.pop()
print(stk.top())
print(stk.empty())
stk.push(4)
print(stk.top())