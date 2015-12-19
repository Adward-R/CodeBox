__author__ = 'Adward'
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)
        '''
        bulbs = [1] * n
        for i in range(2, n):
            #print(bulbs)
            for j in range(n):
                if (j+1) % i == 0:
                    bulbs[j] = 1 - bulbs[j]
        bulbs[-1] = 1 - bulbs[-1]
        return sum(bulbs)
        '''


sol = Solution()
for i in range(1, 50):
    print(str(i) + '|' + str(sol.bulbSwitch(i)))

#3 5 7 9 11 13
#1 2 3 4 5  6