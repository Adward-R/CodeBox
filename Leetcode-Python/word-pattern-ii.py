__author__ = 'Adward'
from collections import defaultdict
class Solution(object):
    def wordPatternMatch0(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        N = len(str)
        if N == 0 or len(pattern) == 0:
            return N == 0 and len(pattern) == 0
        elif N < len(pattern):
            return False
        patFreq = defaultdict(int)
        for ch in pattern:
            patFreq[ch] += 1
        patLength = {}
        unique = list(set(pattern))

        i = 0
        remainL = N
        while True:
            ch = unique[i]
            l = remainL // patFreq[ch]

            if i+1 == len(unique) and remainL and remainL % patFreq[ch] == 0:
                patLength[ch] = l
                bijection = {}
                targets = set()
                start = 0
                for c in pattern:
                    end = start + patLength[c]
                    substr = str[start:end]
                    if c not in bijection:
                        if substr in targets:
                            break
                        bijection[c] = substr
                        targets.add(substr)
                    elif substr != bijection[c]:
                        break
                    start = end
                else:
                    return True
                l = 0

            if l == 0:
                j = i - 1
                while j >= 0 and patLength[unique[j]] <= 1:
                    j -= 1
                if j >= 0:
                    patLength[unique[j]] -= 1
                    remainL += patFreq[unique[j]]
                    i = j + 1
                else:
                    break
            else:
                patLength[ch] = l
                remainL -= l * patFreq[ch]
                i += 1

        return False

    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        bijection = {}
        targets = set()  # to get rid of duplicated target condition such as 'ab' -> 'aa'

        def backTracking(si, pj):
            if si == len(str) and pj == len(pattern):
                return True
            elif si == len(str) or pj == len(pattern):
                return False

            ch = pattern[pj]  # get current pattern character
            if ch in bijection:  # seen this pattern ch before, check if still match
                tgt = bijection[ch]
                if str[si:si+len(tgt)] != tgt:
                    return False
                return backTracking(si + len(tgt), pj + 1)

            # else if haven't seen this pattern ch before
            for k in range(si, len(str)):
                tgt = str[si:k+1]
                if tgt not in targets:
                    bijection[ch] = tgt
                    targets.add(tgt)
                    # continue to match the rest
                    if backTracking(k + 1, pj + 1):
                        return True
                    else:  # backtracking
                        del bijection[ch]
                        targets.remove(tgt)
            # tried best but still no match till the end
            return False

        return backTracking(0, 0)


sol = Solution()
# pattern = "ab"
# str = "aa"
pattern = "ats"
str = "ataa"
print(sol.wordPatternMatch(pattern, str))