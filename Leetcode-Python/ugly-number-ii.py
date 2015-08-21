__author__ = 'Adward'

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        cnt = 0
        nth = 0
        while cnt < n:
            nth = q[0]
            q = q[1:]
            if (nth * 2) not in q:
                q.append(nth * 2)
            if (nth * 3) not in q:
                q.append(nth * 3)
            if (nth * 5) not in q:
                q.append(nth * 5)
            q = sorted(q)
            cnt += 1
        return nth

# (2^x) * (3^y) * (5^z), x,y,z >= 0

sol = Solution()
print(sol.nthUglyNumber(12))

