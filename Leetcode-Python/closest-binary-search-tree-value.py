__author__ = 'Adward'
import bintree_utils
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        p = root
        fathers = []
        while p.left or p.right:
            if target < p.val:
                if p.left:
                    fathers.append(p.val)
                    p = p.left
                else:
                    break
            elif target > p.val:
                if p.right:
                    fathers.append(p.val)
                    p = p.right
                else:
                    break
            else:
                return p.val
        fathers.append(p.val)
        _fathers = [abs(val-target) for val in fathers]
        return fathers[_fathers.index(min(_fathers))]
        # minptr = 0
        # fathers.append(p.val)
        # for i in range(1, len(fathers)):
        #     if abs(fathers[i] - target) < abs(fathers[minptr] - target):
        #         minptr = i
        # return fathers[minptr]

sol = Solution()
codec = bintree_utils.Codec()
root = codec.deserialize('{5,3,6,2,4,#,#,1}')
print(sol.closestValue(root, 2.8))