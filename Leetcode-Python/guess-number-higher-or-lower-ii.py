__author__ = 'Adward'
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DP(s, e):
            # print(s, e)
            if s >= e:
                return 0
            elif table[s][e]:
                return table[s][e]
            else:
                table[s][e] = min((x + max(DP(s, x-1), DP(x+1, e)) for x in range(s, e+1)))
                return table[s][e]

        table = [[None]*(n+1) for _ in range(n+1)]
        return DP(1, n)


sol = Solution()
print(sol.getMoneyAmount(20))