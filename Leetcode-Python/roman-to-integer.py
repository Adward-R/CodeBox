__author__ = 'Adward'

romanNums = [None, 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
                 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        intNum = 0
        tmp = dict[s[0]]
        for i in range(1, len(s)):
            if tmp == 0:
                tmp = dict[s[i]]
            elif tmp < dict[s[i]]:
                intNum += dict[s[i]] - tmp
                tmp = 0
            else:
                intNum += tmp
                tmp = dict[s[i]]
        return intNum + tmp

sol = Solution()
#for romanNum in romanNums[1:]:
#    print(sol.romanToInt(romanNum))
print(sol.romanToInt('MDCCCLXXX'))