__author__ = 'Adward'
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        elif n == 1:
            return True

        leng = len(str(n))
        lastDigit = n % 10
        num = 0
        if lastDigit == 3:
            if leng % 2:
                num = 3 ** (leng * 2 - 1)
            else:
                return False
        elif lastDigit == 9:
            if leng % 2:
                num = 3 ** (leng * 2)
            else:
                return False
        elif lastDigit == 7:
            if leng % 2 == 0:
                num = 3 ** (leng * 2 - 1)
            else:
                return False
        elif lastDigit == 1:
            if leng % 2 == 0:
                num = 3 ** (leng * 2)
            else:
                return False
        else:
            return False

        if num == n:
            return True
        else:
            return False

sol = Solution()
print(sol.isPowerOfThree(3))