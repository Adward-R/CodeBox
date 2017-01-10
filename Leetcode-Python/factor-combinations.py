__author__ = 'Adward'
class Solution(object):

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        DP = {}

        def helper(x):
            from math import sqrt
            if x in DP:
                return DP[x]
            factors = [i for i in range(2, int(sqrt(x))+1) if x % i == 0]
            combs = [[x]]
            for fac in factors:
                for seq in helper(x//fac):
                    if fac <= seq[0]:  # remove duplicates
                        combs.append([fac] + seq)
            DP[x] = combs
            return combs
        return helper(n)[1:]

sol = Solution()
print(sol.getFactors(32))