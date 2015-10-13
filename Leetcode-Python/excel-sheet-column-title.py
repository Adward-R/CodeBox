__author__ = 'Adward'
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        def letterConvert(letter, shamt):
            """
            :param letter: chr
            :param shamt: int
            :return: chr
            """
            i = ord(letter) - ord('A')
            i += shamt
            i %= 26
            return chr(ord('A') + i)

        if n <= 1:
            return 'A'
        title = ''

        while n and n % 26 == 0:
            title = 'Z' + title
            n = int(n / 26) - 1

        while n:
            ch = letterConvert('A', int(n % 26) - 1)
            title = ch + title
            n = int(n / 26)
            while n and n % 26 == 0:
                title = 'Z' + title
                n = int(n / 26) - 1
        return title

sol = Solution()
for i in range(704):
    #if i % 26 == 0:
        print(str(i) + '|' + sol.convertToTitle(i))