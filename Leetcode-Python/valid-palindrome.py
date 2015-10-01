__author__ = 'Adward'

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        leng = len(s)

        p1 = 0
        while p1 < leng and not s[p1].isalnum():
            p1 += 1
        if p1 == leng:
            return True #e.g. #####

        p2 = leng - 1
        while p2 >= 0 and not s[p2].isalnum():
            p2 -= 1

        while p1 < p2:
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                while p1 < p2 and not s[p1].isalnum():
                    p1 += 1
                if p1 == p2:
                    return True
                p2 -= 1
                while p1 < p2 and not s[p2].isalnum():
                    p2 -= 1
                if p1 == p2:
                    return True
        return True #e.g. ###3###

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
#print(sol.isPalindrome("###3a3a####"))