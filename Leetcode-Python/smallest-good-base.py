from math import log
class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """

        '''
        k bases n is 1...1 (m 1s)
        -> means 1 + k + k^2 + ... + k^(m-1) = (k^m - 1) / (k-1) = n
        -> k^m = n(k-1) + 1
        -> n^(1/(m-1)) < k < (n+1)^(1/m)
        '''

        n = int(n)
        max_m = int(log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n ** (m ** (-1)))
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)
        return str(n - 1)
