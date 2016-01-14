__author__ = 'Adward'
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        leng = len(secret)
        flags = [1] * leng
        bullNum = 0
        cowNum = 0
        for i in range(leng):
            if secret[i] == guess[i]:
                bullNum += 1
                flags[i] = 0

        statSecret = [0] * 10
        statGuess = [0] * 10
        for i in range(leng):
            if flags[i]:
                statSecret[int(secret[i])] += 1
                statGuess[int(guess[i])] += 1
        for i in range(10):
            cowNum += min(statSecret[i], statGuess[i])
        return str(bullNum)+'A'+str(cowNum)+'B'

sol = Solution()
print(sol.getHint('11232', '01111'))