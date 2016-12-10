__author__ = 'Adward'
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # also need to check the case when k == 0
        if n == 0:
            return 0
        elif n == 1:
            return k
        same, dif = k, k*(k-1)
        for i in range(3, n+1):
            same, dif = dif, (same+dif)*(k-1)
        return same + dif

sol = Solution()
print(sol.numWays(2, 2))