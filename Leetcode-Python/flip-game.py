__author__ = 'Adward'
class Solution(object):
    def __init__(self):
        self.dict = {
            '+': True,
            '++': False,
            '+++': False,
            '++++': False,
            '+++++': True,
            '++++++': False
        }

    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        nextStrs = set()
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                if 1 < i < len(s) - 3:
                    nextStrs.add(''.join([s[0:i], '--', s[i+2:]]))
                elif i <= 1:
                    nextStrs.add(s[i+2:].lstrip('-'))
                else:
                    nextStrs.add(s[:i].rstrip('-'))
        return nextStrs

    def roundPlay(self, s):  # opponent faces s
        if s in self.dict:
            return self.dict[s]
        strs = self.generatePossibleNextMoves(s)
        for ss in strs:  # self faces ss
            nexts = self.generatePossibleNextMoves(ss)
            if len(nexts) == 0:
                self.dict[s] = False
                return False
            for sss in nexts:
                if self.roundPlay(sss):
                    break
            else:
                self.dict[s] = False
                return False
        self.dict[s] = True
        return True

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for fs in self.generatePossibleNextMoves(s):
            if self.roundPlay(fs):
                return True
        return False


sol = Solution()
# print(sol.generatePossibleNextMoves('+++++++++++++++++++++'))
print(sol.canWin("+++++++++++++++++++++"))
# print(sol.roundPlay(''))