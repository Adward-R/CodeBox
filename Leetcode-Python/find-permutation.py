class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        i, j, n = 0, s.find('D'), len(s)+1
        if j == -1:
            return list(range(1, n+1))
        perm = list(range(1, j+1))
        cur = j+1
        while True:
            i = s.find('I', j)
            if i == -1:
                perm += list(range(n, cur-1, -1))
                break
            perm += list(range(cur+i-j, cur-1, -1))
            cur += i-j+1
            
            j = s.find('D', i)
            if j == -1:
                perm += list(range(cur, n+1))
                break
            perm += list(range(cur, cur+j-i-1))
            cur += j-i-1
        return perm