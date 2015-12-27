__author__ = 'Adward'
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # -(-(3-5)+10-2) = +(+(3-5)-10+2)
        ssum = [0]
        ssign = [1]
        tmpN = 0

        for ch in s:
            if ch == '(':
                ssum.append(0)
                ssign.append(1)
            elif ch == ')':
                ssum[-1] += ssign[-1] * tmpN
                tmpN = 0
                tmp = ssum[-1]
                ssum.pop()
                ssign.pop()
                ssum[-1] += ssign[-1] * tmp
            elif ch != ' ':
                if ch.isdigit():
                    tmpN = tmpN * 10 + int(ch)
                else:
                    ssum[-1] += ssign[-1] * tmpN
                    tmpN = 0
                    if ch == '+':
                        ssign[-1] = 1
                    else:
                        ssign[-1] = -1
        if tmpN:
            ssum[0] += ssign[-1] * tmpN
        return ssum[0]

sol = Solution()
#print(sol.calculate('(1+(4+5+2)-3)-(6+8)'))
print(sol.calculate('2-(5-6)'))