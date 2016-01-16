__author__ = 'Adward'
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        digits = [i+1 for i in range(n)]
        per = ''
        last = n
        mul = 1
        for i in range(2, last):
            mul *= i
        for i in range(n-1):
            idx = (k-1) // mul
            per += str(digits[idx])
            del digits[idx]
            k %= mul
            mul //= (last-1)
            last -= 1
        return per + str(digits[0])

sol = Solution()
print(sol.getPermutation(1,2))