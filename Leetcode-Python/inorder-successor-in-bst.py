__author__ = 'Adward'
import bintree_utils

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        ptr = root
        path = []
        while ptr.val != p.val:
            path.append(ptr)
            ptr = ptr.left if ptr.val > p.val else ptr.right
        if ptr.right:
            ptr = ptr.right
            while ptr.left:
                ptr = ptr.left
            return ptr
        else:
            while len(path) and path[-1].val < ptr.val:
                path.pop()
            return path[-1] if len(path) else None
            
        # fathers = []
        # ptr = root
        # while ptr.val != p.val:
        #     fathers.append(ptr)
        #     if ptr.val > p.val:
        #         ptr = ptr.left
        #     else:
        #         ptr = ptr.right

        # if len(fathers) and p.val < fathers[-1].val:
        #     choice1 = fathers[-1]
        #     if p.right:
        #         choice2 = p.right
        #         while choice2.left:
        #             choice2 = choice2.left
        #         if choice1.val < choice2.val:
        #             return choice1
        #         else:
        #             return choice2
        #     else:
        #         fathers.pop()
        #         return choice1
        # elif p.right:
        #     choice2 = p.right
        #     while choice2.left:
        #         choice2 = choice2.left
        #     return choice2
        # else:
        #     try:
        #         ptr = fathers[-1]
        #     except:
        #         return None
        #     while len(fathers) > 1 and ptr.val < p.val:
        #         fathers.pop()
        #         ptr = fathers[-1]
        #     if len(fathers) and ptr.val > p.val:
        #         return ptr
        #     else:
        #         return None


sol = Solution()
codec = bintree_utils.Codec()
# treestr = '{5,3,6,2,4,#,#,1}'
# treestr = '{5,3,6,1,4,#,#,#,2}'
treestr = '{3,2,4,1}'
root = codec.deserialize(treestr)
node = root.left.left
for i in range(3):
    node = sol.inorderSuccessor(root, node)
    print(node.val)