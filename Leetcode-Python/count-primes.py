__author__ = 'Adward'
class Solution(object):
    def countPrimes(self, n): #using [Sieve of Eratosthenes]
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        tbl = [1] * n
        tbl[0] = tbl[1] = 0
        prime = 2
        limit = int(n/2)+1
        while prime < limit:
            num = prime * 2
            while num < n:
                tbl[num] = 0
                num += prime
            prime += 1
            while prime < n and tbl[prime] == 0:
                prime += 1
        return sum(tbl)

sol = Solution()
for i in range(31):
    print(str(i) + '|' + str(sol.countPrimes(i)))