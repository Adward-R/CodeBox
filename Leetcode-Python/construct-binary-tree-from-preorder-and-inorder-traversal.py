__author__ = 'Adward'

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return
        print(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        midVal = preorder[0]
        root = TreeNode(midVal)
        midIdx = inorder.index(midVal)
        del preorder[0]
        root.left = self.buildTree(preorder, inorder[0:midIdx])
        root.right = self.buildTree(preorder, inorder[midIdx+1:])
        return root

sol = Solution()
#root = sol.buildTree([1,2,7,4,5,3,6,8,9], [7,2,5,4,1,3,8,6,9])
root = sol.buildTree([], [])
sol.preorderTraversal(root)
print('===')
sol.inorderTraversal(root)