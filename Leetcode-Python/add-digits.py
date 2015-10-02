__author__ = 'Adward'

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        remains = num % 9
        if remains == 0:
            if num == 0:
                return 0
            else:
                return 9
        else:
            return remains

sol = Solution()
print(sol.addDigits(123456))