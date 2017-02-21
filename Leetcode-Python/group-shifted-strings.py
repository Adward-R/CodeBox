__author__ = 'Adward'


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for s in strings:
            shamt = ord('a') - ord(s[0])
            if shamt != 0:
                key = ''.join(
                    chr(ord('a') + (ord(ch) - ord('a') + shamt) % 26)
                    for ch in s
                )
            else:
                key = s
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        return groups.values()

sol = Solution()
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(sol.groupStrings(strings))