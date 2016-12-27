__author__ = 'Adward'
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 1:
            if n % 2:
                if n != 3 and n & 2:  # second LSB
                    n += 1
                else:
                    n -= 1
            else:
                n /= 2
            cnt += 1
        return cnt