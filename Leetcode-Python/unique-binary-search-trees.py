__author__ = 'Adward'
from itertools import permutations

class Solution(object):
    '''
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def binTreeSerial2RecLeft(self, node):
        if not node:
            self.res += '#,'
            return
        self.res += str(node.val) + ','
        self.binTreeSerial2RecLeft(node.left)
        self.binTreeSerial2RecLeft(node.right)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.res = ''
        self.binTreeSerial2RecLeft(p)
        tmp = self.res
        self.res = ''
        self.binTreeSerial2RecLeft(q)
        #print(tmp)
        #print(self.res)
        if tmp == self.res:
            return True
        else:
            return False

    def numTrees0(self, n):
        """
        :type n: int
        :rtype: int
        """
        perm = list(permutations([i for i in range(1, n+1)]))
        roots = []
        for seq in perm:
            roots.append(self.TreeNode(seq[0]))
            for val in seq[1:]:
                ptr = roots[-1]
                while True:
                    if ptr.val > val:
                        if ptr.left:
                            ptr = ptr.left
                        else:
                            ptr.left = self.TreeNode(val)
                            break
                    else:
                        if ptr.right:
                            ptr = ptr.right
                        else:
                            ptr.right = self.TreeNode(val)
                            break

        ress = []
        for i in range(len(roots)):
            self.res = ''
            self.binTreeSerial2RecLeft(roots[i])
            #print(perm[i])
            ress.append(self.res)
        for i in range(len(ress)):
            for j in range(i+1,len(ress)):
                if ress[i] == ress[j]:
                    ress[j] = None
        nts = 0
        for r in ress:
            if r:
                nts += 1
        return nts
    '''
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        nts = [1, 1] + [0] * (n-1)
        for i in range(2, n+1):
            for j in range(int(i/2)):
                nts[i] += 2 * nts[i-1-j] * nts[j]
            if i % 2 == 1:
                nts[i] += nts[int(i/2)] ** 2
        return nts[-1]


sol = Solution()
for i in range(10):
    print(sol.numTrees(i))
