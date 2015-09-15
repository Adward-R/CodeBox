__author__ = 'Adward'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    maxDep = 0
    currentDep = 0

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
        if not node:
            if self.currentDep-1 > self.maxDep:
                self.maxDep = self.currentDep-1
                #self.currentDep -= 1
            return

        self.currentDep += 1
        self.binTreeDepthFirstTraversal(node.left)
        self.binTreeDepthFirstTraversal(node.right)
        self.currentDep -= 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.currentDep = 1
        self.maxDep = 1
        self.binTreeDepthFirstTraversal(root)
        return self.maxDep

sol = Solution()
head = sol.binTreeBuild("{1}")
print(sol.maxDepth(head))