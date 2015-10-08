__author__ = 'Adward'
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
firstBad = 1

def isBadVersion(version):
    if 1 <= version < firstBad:
        return False
    else:
        return True

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right - left > 1:
            mid = int((left+right)/2)
            if isBadVersion(mid):
                right = mid
            else:
                left = mid

        if isBadVersion(left):
            return left
        else:
            return right

sol = Solution()
print(sol.firstBadVersion(10))