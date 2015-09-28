__author__ = 'Adward'

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)

    def postorderTraversal(self, root):
        if root is None:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val)

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        midVal = postorder[-1]
        root = TreeNode(midVal)
        midIdx = inorder.index(midVal)
        postorder.pop()
        root.right = self.buildTree(inorder[midIdx+1:], postorder)
        root.left = self.buildTree(inorder[0:midIdx], postorder)
        return root

sol = Solution()
root = sol.buildTree([7,2,5,4,1,3,8,6,9], [7,5,4,2,8,9,6,3,1])
#root = sol.buildTree([], [])
sol.postorderTraversal(root)
print('===')
sol.inorderTraversal(root)