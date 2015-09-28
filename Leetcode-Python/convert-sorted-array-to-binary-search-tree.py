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

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        leng = len(nums)
        if leng == 0:
            return None
        elif leng == 1:
            return TreeNode(nums[0])
        else:
            mid = int(leng/2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root

sol = Solution()
root = sol.sortedArrayToBST([1,2,3,4,5,6,7,8])
#root = sol.buildTree([])
sol.postorderTraversal(root)
print('===')
sol.inorderTraversal(root)