__author__ = 'Adward'
from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        sz = len(primes)
        q = [(1, 0)]
        num, curMax = 0, 1
        for _ in range(n):
            num, bound = heappop(q)
            for i in range(bound, sz):
                new = num * primes[i]
                if new > curMax:  # to avoid memory exceed
                    if len(q) >= n:
                        break
                    else:
                        curMax = new
                heappush(q, (new, i))
        return num


sol = Solution()
primes = [2,3,5,13,19,29,31,41,43,53,59,73,83,89,97,103,107,109,127,137,139,149,163,173,179,193,197,199,211,223,227,229,239,241,251,257,263,269,271,281,317,331,337,347,353,359,367,373,379,389,397,409,419,421,433,449,457,461,463,479,487,509,521,523,541,547,563,569,577,593,599,601,613,619,631,641,659,673,683,701,709,719,733,739,743,757,761,769,773,809,811,829,857,859,881,919,947,953,967,971]
print(sol.nthSuperUglyNumber(4000, primes))
