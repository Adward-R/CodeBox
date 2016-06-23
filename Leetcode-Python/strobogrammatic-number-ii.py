__author__ = 'Adward'


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        elif n == 1:
            return ['0', '1', '8']
        stro_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        half = n // 2
        # max_in_half = 10 ** half
        # stro_dict = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        q = ['1', '6', '8', '9']
        while len(q[0]) < half:
            for key in stro_dict:
                q.append(q[0] + key)
            q = q[1:]
        if n % 2:
            rstrs = []
            for mid in ['0', '1', '8']:
                rstrs += [num + mid + ''.join([stro_dict[ch] for ch in num[::-1]]) for num in q]
            return rstrs
        else:
            return [num + ''.join([stro_dict[ch] for ch in num[::-1]]) for num in q]

sol = Solution()
print(sol.findStrobogrammatic(7))