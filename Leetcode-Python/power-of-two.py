class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pwr = 1
        while pwr < n:
        	pwr *= 2
        if pwr == n:
        	return True
        else:
        	return False
sol = Solution()
print(sol.isPowerOfTwo(-8))