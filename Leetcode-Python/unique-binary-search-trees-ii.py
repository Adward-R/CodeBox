__author__ = 'Adward'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def serialTree(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = '{'
        tmp = ''
        q = [root]
        while len(q):
            if q[0]:
                res += tmp + str(q[0].val) + ','
                q.append(q[0].left)
                q.append(q[0].right)
                tmp = ''
            else:
                tmp += '#,'
            q = q[1:]

        return res[0:-1] + '}'

    def copyTrees(self, n, shamt):
        """
        :type n: int
        :type shamt: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return [None]
        elif n == 1:
            return [TreeNode(shamt+1)]
        roots = []
        for i in range(1, n+1):
            for rleft in self.copyTrees(i-1, shamt):
                for rright in self.copyTrees(n-i, i+shamt):
                    roots.append(TreeNode(i+shamt))
                    roots[-1].left = rleft
                    roots[-1].right = rright
        return roots

    def generateTrees0(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.copyTrees(n, 0)

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [[[] for j in range(n)] for i in range(n)]  # dp[i][j] <= helper(i+1, j+1)

        def helper(s, e):  # rtype: List[TreeNode]
            if s > e:
                return [None]
            elif dp[s-1][e-1]:
                return dp[s-1][e-1]
            ret = []
            for rval in range(s, e+1):
                for left in helper(s, rval-1):
                    for right in helper(rval+1, e):
                        root = TreeNode(rval)
                        root.left = left
                        root.right = right
                        ret.append(root)
            dp[s-1][e-1] = ret
            return ret

        return helper(1, n) if n else []

sol = Solution()
cnt = 0
for root in sol.generateTrees(6):
    print(sol.serialTree(root))
    cnt += 1
print(cnt)