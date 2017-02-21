__author__ = 'Adward'
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

picked = 6


def guess(num):
    if num > picked:
        return -1
    elif num < picked:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left + 1 < right:
            mid = (left + right) // 2
            comp = guess(mid)
            if comp == 1:
                left = mid
            elif comp == -1:
                right = mid
            else:
                return mid
        if guess(left) == 0:
            return left
        else:
            return right

sol = Solution()
print(sol.guessNumber(10))