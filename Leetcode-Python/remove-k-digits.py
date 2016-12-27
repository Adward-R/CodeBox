__author__ = 'Adward'
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        m = len(num)
        if m == k:
            return '0'
        toDel = set()
        ascend = []
        for i, c in enumerate(num):
            n = int(c)
            while len(toDel) < k and len(ascend) and n < ascend[-1][1]:
                toDel.add(ascend.pop()[0])
            ascend.append((i, n))
            if len(toDel) == k:
                break
        else:
            for _ in range(k-len(toDel)):
                toDel.add(ascend.pop()[0])

        ret = ''.join((num[i] for i in range(m) if i not in toDel))
        i = 0
        while i < len(ret) and ret[i] == '0':
            i += 1
        if i == len(ret):
            return '0'
        else:
            return ret[i:]
