__author__ = 'Adward'
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(w):
            p1, p2 = 0, len(w)-1
            while p1 < p2:
                if w[p1] != w[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True

        ans = []
        word2Ind = {}
        for i in range(len(words)):
            word2Ind[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):  # pay attention to this range
                s1 = words[i][:j]
                s2 = words[i][j:]
                if isPalindrome(s1):
                    s2rev = ''.join(reversed(s2))
                    if s2rev in word2Ind:
                        rev_i = word2Ind[s2rev]
                        if rev_i != i:
                            ans.append([rev_i, i])
                if isPalindrome(s2) and len(s2):  # check len(s2) to avoid duplicates
                    s1rev = ''.join(reversed(s1))
                    if s1rev in word2Ind:
                        rev_i = word2Ind[s1rev]
                        if rev_i != i:
                            ans.append([i, rev_i])
        return ans


    def palindromePairs2(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        pairs = set()

        def match():
            wordsDict = {}

            for ind in range(len(words)):
                w = words[ind]

                if len(w) == 1:
                    wordsDict[w] = (1, ind)
                    continue
                elif len(w) == 2:
                    wordsDict[w] = (2 if w[0] == w[1] else 1, ind)
                    continue

                pmid_odd = 2
                while True:
                    for i in range(pmid_odd-1):
                        if w[-pmid_odd-i-1] != w[-pmid_odd+i+1]:
                            break
                    else:
                        pmid_odd += 1
                        continue
                    break
                pmid_odd -= 1

                pmid_even = 1
                while True:
                    for i in range(pmid_even):
                        if w[-pmid_even-i-1] != w[-pmid_even+i]:
                            break
                    else:
                        pmid_even += 1
                        continue
                    break
                pmid_even -= 1

                wordsDict[w] = (max(pmid_odd*2-1, pmid_even*2), ind)

            for ind in range(len(words)):
                w = words[ind]
                plen, _ = wordsDict[w]
                rev = w[::-1]
                for sind in {0, 1, plen}:
                    rw = rev[sind:]
                    if rw in wordsDict:
                        ind2 = wordsDict[rw][1]
                        if ind != ind2:
                            pairs.add((ind, ind2))

        match()
        words = [w[::-1] for w in words]
        match()
        return pairs

words = ["abcd", "dcba", "lls", "s", "sssll"]
sol = Solution()
print(sol.palindromePairs(words))