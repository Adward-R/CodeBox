__author__ = 'Adward'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binTreeBuild(self, nodesLst):
        """
        :type nodesLst: str
        :rtype: TreeNode
        """
        lst = nodesLst[1:-1].split(',')
        if not lst[0].isdigit():
            return None
        head = TreeNode(lst[0])
        q = [head]
        onLeft = True
        for num in lst[1:]:
            if num.isdigit():
                if onLeft:
                    q[0].left = TreeNode(int(num))
                    onLeft = False
                    q.append(q[0].left)
                else:
                    q[0].right = TreeNode(int(num))
                    onLeft = True
                    q.append(q[0].right)
                    q = q[1:]
            else:
                if onLeft:
                    onLeft = False
                else:
                    onLeft = True
                    q = q[1:]

        return head

    res = ''

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
        print(tmp)
        print(self.res)
        if tmp == self.res:
            return True
        else:
            return False

sol = Solution()
p = sol.binTreeBuild("{1,2,2,3,4,4,3}")
q = sol.binTreeBuild("{1,2,2,3,4,4,3}")
print(sol.isSameTree(p, q))