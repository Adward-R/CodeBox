class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = n ** 0.5
        maxBase = int(base)
        if base == maxBase: #cannot use in cpp
            return 1
        for i in range(2, n+1):
            stk = [maxBase]
            sqrsum = maxBase ** 2
            for j in range(i-1):
                stk.append(int((n - sqrsum) ** 0.5))
                sqrsum += stk[-1] ** 2

            reachFlag = True
            while sqrsum != n:
                sqrsum -= stk[-1] ** 2
                stk.pop()
                while len(stk) and stk[-1] == 1:
                    sqrsum -= 1
                    stk.pop()
                if len(stk) == 0:
                    reachFlag = False
                    break
                sqrsum -= stk[-1] ** 2
                stk[-1] -= 1
                sqrsum += stk[-1] ** 2
                for j in range(i-len(stk)):
                    tail = int((n - sqrsum) ** 0.5)
                    if tail > stk[-1]:
                        tail = stk[-1]
                    sqrsum += tail ** 2
                    stk.append(tail)
                #print(stk)
            if reachFlag:
                return i

sol = Solution()
print(sol.numSquares(192))
