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

    def binTreeSerial1(self, head): #level-order
        """
        :type head: TreeNode
        :rtype: str
        """
        res = '{'
        q = [head]
        while len(q) != 0:
            res += str(q[0].val) + ','
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q = q[1:]
        res = res[0:-1]
        res += '}'
        return res

    res = ''

    def binTreeSerial2RecLeft(self, node):
        if not node:
            self.res += '#,'
            return
        self.res += str(node.val) + ','
        self.binTreeSerial2RecLeft(node.left)
        self.binTreeSerial2RecLeft(node.right)

    def binTreeSerial2RecRight(self, node):
        if not node:
            self.res += '#,'
            return
        self.res += str(node.val) + ','
        self.binTreeSerial2RecRight(node.right)
        self.binTreeSerial2RecRight(node.left)

    def binTreeSerial2(self, head): #pre-order
        """
        :type head: TreeNode
        :rtype: str
        """
        self.res = ''
        self.binTreeSerial2RecLeft(head)
        return self.res

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = ''
        self.binTreeSerial2RecLeft(root)
        tmp = self.res
        self.res = ''
        self.binTreeSerial2RecRight(root)
        print(tmp)
        print(self.res)
        return (tmp == self.res)


sol = Solution()
head = sol.binTreeBuild("{1,2,2,3,4,4,3}")
print(sol.isSymmetric(head))