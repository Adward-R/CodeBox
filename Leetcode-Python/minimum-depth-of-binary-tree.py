__author__ = 'Adward'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.minDep = 0
        self.currentDep = 0

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

    def binTreeDepthFirstTraversal(self, node):
        if not node.left and not node.right:
            if self.currentDep < self.minDep:
                self.minDep = self.currentDep
            return

        self.currentDep += 1
        if node.left:
            self.binTreeDepthFirstTraversal(node.left)
        if node.right:
            self.binTreeDepthFirstTraversal(node.right)
        self.currentDep -= 1

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.currentDep = 1
        self.minDep = 65535
        self.binTreeDepthFirstTraversal(root)
        return self.minDep

sol = Solution()
head = sol.binTreeBuild("{1,2,#,#,3,4}")
print(sol.minDepth(head))