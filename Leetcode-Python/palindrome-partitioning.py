__author__ = 'Adward'
import copy
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def concatIndex(invIdx, start, lens, par):
            if start == lens:
                self.par.append(copy.deepcopy(par))
            else:
                for end in invIdx[start]:
                    par.append(s[start:end])
                    concatIndex(invIdx, end, lens, par)
                    par.pop()

        lens = len(s)
        if lens == 0:
            return []
        chIdx = {}
        for i in range(lens):
            if s[i] in chIdx.keys():
                chIdx[s[i]].append(i)
            else:
                chIdx[s[i]] = [i]

        invIdx = []
        for i in range(lens):
            invIdx.append([i+1])
        for key in chIdx:
            chFreq = len(chIdx[key])
            for i in range(0, chFreq-1):
                for j in range(i+1, chFreq):
                    _i = chIdx[key][i]+1
                    _j = chIdx[key][j]-1
                    if _i > _j:
                        invIdx[_i-1].append(_j+2)
                    else:
                        while _i < _j:
                            if s[_i] == s[_j]:
                                _i += 1
                                _j -= 1
                            else:
                                break
                        if _i >= _j:
                            invIdx[chIdx[key][i]].append(chIdx[key][j]+1)
        #print(invIdx)
        self.par = []
        par = []
        concatIndex(invIdx, 0, lens, par)
        return self.par

sol = Solution()
s = 'a'
print(sol.partition(s))