__author__ = 'Adward'
from collections import defaultdict
from heapq import *
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(points) <= 1:
            return True
        x_ref = (min(points, key=lambda pt: pt[0])[0] + max(points, key=lambda pt: pt[0])[0]) * 1.0 / 2
        horizon = defaultdict(list)
        for x, y in points:
            heappush(horizon[y], x)
        for y in horizon:
            stk = []
            prev_x = -1 << 31
            while len(horizon[y]):
                x = heappop(horizon[y])
                if x != prev_x:
                    prev_x = x
                    if x < x_ref:
                        stk.append(x)
                    elif x > x_ref:
                        if len(stk) == 0 or stk[-1] + x != 2 * x_ref:
                            return False
                        else:
                            stk.pop()
        return True

sol = Solution()
points = [[[-16,1],[16,1],[16,1]]]
print(sol.isReflected(points))