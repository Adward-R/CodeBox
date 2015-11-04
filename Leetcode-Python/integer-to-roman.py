__author__ = 'Adward'
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

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1 or num > 3999:
            return None
        dict3 = [(1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]
        dict1 = [(900, 'CM'), (400, 'CD'), (90, 'XC'), (40, 'XL'), (9, 'IX'), (4, 'IV')]
        s = ''
        for i in range(6):
            n = int(num / dict3[i][0])
            num -= n * dict3[i][0]
            for j in range(n):
                s += dict3[i][1]
            ###
            if dict1[i][0] <= num:
                num -= dict1[i][0]
                s += dict1[i][1]
        for i in range(num):
            s += 'I'
        return s

sol = Solution()
for i in range(1, 4000):
    if i != sol.romanToInt(sol.intToRoman(i)):
        print(i)