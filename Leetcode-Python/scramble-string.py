__author__ = 'Adward'
class Solution(object):
    # Determine if s2 is a scrambled string of s1
    # Bottom-up DP ver
    def isScrambleBottonUp(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        sSize = len(s1)
        if sSize == 0:
            return True
        elif sSize == 1:
            return s1 == s2
        # isS[L][i][j] indicates isScramble(s1[i:i+L], s2[j:j+L])
        isS = [[[False] * sSize for j in range(sSize)] for i in range(sSize+1)]
        # boundary
        for i in range(sSize):
            for j in range(sSize):
                isS[1][i][j] = s1[i] == s2[j]

        for L in range(2, sSize+1):
            for i in range(sSize-L+1):
                for j in range(sSize-L+1):
                    for k in range(1, L):
                        if isS[L][i][j]:
                            break
                        isS[L][i][j] |= isS[k][i][j] and isS[L-k][i+k][j+k]
                        isS[L][i][j] |= isS[k][i+L-k][j] and isS[L-k][i][j+k]
        return isS[sSize][0][0]

    def isScrambleDP(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        isScramblePair = {}

        def helper(s1, s2):
            sSize = len(s1)
            if sSize == 0:
                return True
            elif sSize == 1:
                return s1 == s2

            res = False
            if s1 + s2 in isScramblePair:
                return isScramblePair[s1 + s2]
            if s1 == s2:
                res = True

            i = 0
            while i+1 < sSize and not res:
                res |= helper(s1[0:i+1], s2[0:i+1]) and helper(s1[i:sSize-i], s2[i:sSize-1])
                res |= helper(s1[0:i+1], s2[sSize-i:i]) and helper(s1[i:sSize-i], s2[0:sSize-i])
                i += 1
            isScramblePair[s1+s2] = res
            return res

        return helper(s1, s2)

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        sSize = len(s1)
        cnt = [0] * 26
        for i in range(sSize):
            cnt[ord(s1[i])-ord('a')] += 1
            cnt[ord(s2[i])-ord('a')] -= 1
        for i in range(26):
            if cnt[i] != 0:
                return False
        for i in range(1, sSize):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[sSize-i:]) and self.isScramble(s1[i:], s2[:sSize-i]):
                return True
        return False

sol = Solution()
print(sol.isScramble("aa", "ab"))