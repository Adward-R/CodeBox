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
        if (not lst[0].isdigit()) and (not lst[0][1:].isdigit()):
            return None
        head = TreeNode(int(lst[0]))
        q = [head]
        onLeft = True
        for num in lst[1:]:
            if num.isdigit() or num[1:].isdigit():
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

    currentSum = 0
    sums = []

    def binTreeDepthFirstTraversal(self, node):
        if not node.left and not node.right:
            self.sums.append(self.currentSum * 10 + node.val)
            return
        self.currentSum = self.currentSum * 10 + node.val
        if node.left:
            self.binTreeDepthFirstTraversal(node.left)
        if node.right:
            self.binTreeDepthFirstTraversal(node.right)
        self.currentSum /= 10

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.currentSum = 0
        self.sums = []
        self.binTreeDepthFirstTraversal(root)
        return int(sum(self.sums))

sol = Solution()
root = sol.binTreeBuild('{1,2,3,4,#,#,5}')
print(sol.sumNumbers(root))