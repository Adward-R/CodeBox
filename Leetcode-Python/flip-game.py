__author__ = 'Adward'
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        nextStrs = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                nextStrs.append(''.join([s[0:i], '--', s[i+2:]]))
        return nextStrs

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        firstSteps = self.generatePossibleNextMoves(s)
        for fs in firstSteps:  # opponents faces 'fs'
            try:
                q = self.generatePossibleNextMoves(fs)
                curntLeng = len(q)
                while curntLeng:
                    for k in range(curntLeng):
                        # self faces q[k]
                        strs = self.generatePossibleNextMoves(q[k])
                        if len(strs) == 0:
                            raise
                        for ss in strs:  # opponent faces ss
                            rtstrs = self.generatePossibleNextMoves(ss)
                            if len(rtstrs):
                                q += rtstrs
                    q = q[curntLeng:]
                    curntLeng = len(q)
                return True
            except:
                pass
        return False




sol = Solution()
# print(sol.generatePossibleNextMoves('++++'))
print(sol.canWin('++++-++++++'))