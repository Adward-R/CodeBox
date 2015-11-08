__author__ = 'Adward'

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = []
        tmpNum = 0
        for ch in s:
            if ch != ' ':
                if ch.isdigit():
                    tmpNum = tmpNum * 10 + int(ch)
                else:
                    lst.append(str(tmpNum))
                    tmpNum = 0
                    lst.append(ch)
        lst.append(str(tmpNum))
        for i in range(len(lst)-1):
            if lst[i] == '*':
                lst[i+1] = str(int(lst[i+1]) * int(lst[i-1]))
                lst[i-1] = lst[i] = None
            elif lst[i] == '/':
                lst[i+1] = str(int(lst[i-1]) / int(lst[i+1]))
                lst[i-1] = lst[i] = None

        #print(lst)
        for i in range(len(lst)-1):
            if lst[i] == '+' or lst[i] == '-':
                j = i + 1
                while lst[j] is None:
                    j += 1
                k = i - 1
                while lst[k] is None:
                    k -= 1
                if lst[i] == '+':
                    lst[j] = str(int(lst[j]) + int(lst[k]))
                else:
                    lst[j] = str(int(lst[k]) - int(lst[j]))

        return int(lst[-1])

sol = Solution()
print(sol.calculate('0*0'))