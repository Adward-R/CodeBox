__author__ = 'Adward'
class Solution(object):
    def calculate(self, s):
        stk = []
        num, sign, result = 0, 1, 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+' or ch == '-':
                result += sign * num
                num = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                stk += [result, sign]
                result, sign = 0, 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stk.pop()  # set the sign of result in current ()
                result += stk.pop()  # before the sign is the last result calculated in outer scope

        if num:
            result += sign * num
        return result

    def calculate1(self, s):
        seq = ''
        balance = 0
        i = 0
        while i < len(s):
            if s[i] == '-':
                seq += '+' if balance % 2 else '-'
                if i + 1 < len(s) and s[i + 1] == '(':
                    balance += 1
            elif s[i] == ')' and balance > 0:
                balance -= 1
            elif s[i] == '+':
                seq += '-' if balance % 2 else '+'
            elif s[i].isdigit():
                seq += s[i]
            i += 1
        ret = 0
        for subseq in seq.split('+'):
            sublist = [int(d) for d in subseq.split('-')]
            ret += sublist[0] - sum(sublist[1:])
        return ret

    def calculate0(self, s):
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
print(sol.calculate('(1+(4+5+2)-3)-(6+8)'))
print(sol.calculate('1-(2-(3-4)-5)'))