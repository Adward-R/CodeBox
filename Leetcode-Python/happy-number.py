__author__ = 'Adward'

class Solution(object):
    def sumOfSqDigits(self, num):
        sum = 0
        while num != 0:
            rem = num % 10
            num = int(num/10)
            sum += rem * rem
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cnt = 0
        while n != 1 and cnt < 9:
            n = self.sumOfSqDigits(n)
            print(n)
            cnt += 1

        res = False
        if n == 1:
            res = True

        return res

sol = Solution()
'''
maxCycles = 0
for i in range(10, 2147483647):
    cycles = sol.isHappy(i)[1]
    if cycles < 50 and cycles > maxCycles:
        maxCycles = cycles
print(maxCycles)
'''
sol.isHappy(2147483647)