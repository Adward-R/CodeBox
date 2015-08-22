__author__ = 'Adward'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashtblS = {}
        for ch in s:
            if ch in hashtblS.keys():
                hashtblS[ch] += 1
            else:
                hashtblS[ch] = 0

        hashtblT = {}
        for ch in t:
            if ch in hashtblT.keys():
                hashtblT[ch] += 1
            else:
                hashtblT[ch] = 0

        for key in hashtblS:
            if key not in hashtblT:
                return False
            else:
                if hashtblS[key] != hashtblT[key]:
                    return False

        return True


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))