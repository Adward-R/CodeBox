__author__ = 'Adward'
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

    def __init__(self):
        res = 0
        cnt = 0

    def depthFirst(self, node):
        if node is None:
            return
        else:
            self.depthFirst(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return
            self.depthFirst(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.cnt = k
        self.depthFirst(root)
        res = self.res
        self.res = 0
        return res

sol = Solution()
root = sol.binTreeBuild('{5,3,7,2,4,6,8,1}')
print(sol.kthSmallest(root, 7))