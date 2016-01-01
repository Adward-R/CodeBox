__author__ = 'Adward'
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        BASE_A = ord('a')
        N_LETTERS = 26
        alphabet = []
        used = [False] * N_LETTERS

        for i in range(N_LETTERS):
            alphabet.append([])
        for i in range(len(s)):
            alphabet[ord(s[i]) - BASE_A].append(i)

        totalLeng = 0
        #smallestRightMost = len(s) - 1
        for i in range(N_LETTERS):
            if len(alphabet[i]):
                pass#totalLeng += 1
            else:
                used[i] = True
                #tmp = alphabet[i][-1]
                #if tmp < smallestRightMost:
                    #smallestRightMost = tmp

        rightMosts = []
        for lst in alphabet:
            if len(lst):
                rightMosts.append(lst[-1])
        #rightMosts.sort(reverse=True)

        seq = ''
        curRightMost = -1

        for i in range(N_LETTERS):
            flag = False
            for j in range(N_LETTERS):
                if not used[j] and alphabet[j][-1] > curRightMost:
                    for idx in alphabet[j]:
                        mmin = min(rightMosts)
                        if curRightMost < idx <= mmin: #- totalLeng + curLeng + 1:
                            curRightMost = idx
                            used[j] = True
                            seq += chr(BASE_A + j)
                            #if alphabet[j][-1] == rightMosts[-1]:
                            #    rightMosts.pop()
                            del rightMosts[rightMosts.index(alphabet[j][-1])]
                            flag = True
                            break
                if flag:
                    break
        return seq

sol = Solution()
#print(sol.removeDuplicateLetters('cbacdcbc'))
print(sol.removeDuplicateLetters("caccabad"))