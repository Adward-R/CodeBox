__author__ = 'Adward'

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapdict = {}
        for i in range(len(s)):
            try:
                ch = mapdict[s[i]]
                if ch != t[i]:
                    return False
            except:
                if t[i] in list(mapdict.values()):
                    return False
                else:
                    mapdict[s[i]] = t[i]
        return True

sol = Solution()
print(sol.isIsomorphic('add', 'egg'))
print(sol.isIsomorphic('foo', 'bar'))
print(sol.isIsomorphic('paper', 'title'))
print(sol.isIsomorphic('', ''))
print(sol.isIsomorphic('ab', 'aa'))