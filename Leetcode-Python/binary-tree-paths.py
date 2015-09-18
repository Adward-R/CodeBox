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

    binTreePaths = []

    def binTreePreorder(self, node, prePath):
        if (not node.left) and (not node.right): #is leaf
            self.binTreePaths.append(prePath+'->'+str(node.val))
        else:
            if node.left:
                self.binTreePreorder(node.left, prePath+'->'+str(node.val))
            if node.right:
                self.binTreePreorder(node.right, prePath+'->'+str(node.val))

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.binTreePaths = []
        if not root:
            return []
        if (not root.left) and (not root.right): #is leaf
            return [str(root.val)]
        if root.left:
            self.binTreePreorder(root.left, str(root.val))
        if root.right:
            self.binTreePreorder(root.right, str(root.val))
        return self.binTreePaths

sol = Solution()
root = sol.binTreeBuild("{1,2,#,3}")
print(sol.binaryTreePaths(root))