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

    def findBSTmin(self, root):
        if not root.left:
            return root
        else:
            return self.findBSTmin(root.left)

    def findBSTmax(self, root):
        if not root.right:
            return root
        else:
            return self.findBSTmax(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left:
            if root.right:
                if self.isValidBST(root.left) \
                        and self.isValidBST(root.right) \
                        and int(root.val) > self.findBSTmax(root.left).val \
                        and int(root.val) < self.findBSTmin(root.right).val:
                    return True
                else:
                    return False
            else:
                if self.isValidBST(root.left) \
                        and int(root.val) > self.findBSTmax(root.left).val:
                    return True
                else:
                    return False
        else:
            if root.right:
                if self.isValidBST(root.right) \
                        and int(root.val) < self.findBSTmin(root.right).val:
                    return True
                else:
                    return False
            else:
                return True

sol = Solution()
root = sol.binTreeBuild("{10,5,15,#,#,6,20}")
print(sol.isValidBST(root))