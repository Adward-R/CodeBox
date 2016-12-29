__author__ = 'Adward'
from heapq import *
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        hp = []
        for s, e, inc in updates:
            heappush(hp, (s, inc))
            heappush(hp, (e+1, -inc))
        slots = []
        last_ind = -1
        while len(hp):
            ind, inc = heappop(hp)
            if ind == last_ind:
                slots[-1][1] += inc
            else:
                slots.append([ind, inc])
            last_ind = ind
        # print(slots)
        arr = []
        s, inc = 0, 0
        for e, _inc in slots:
            arr += [inc] * (e-s)
            s = e
            inc += _inc
        return arr + [0] * (length - s)

sol = Solution()
updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
]  # [-2, 0, 3, 5, 3]
# updates = [[2,4,6],[5,6,8],[1,9,-4]]
print(sol.getModifiedArray(10, updates))