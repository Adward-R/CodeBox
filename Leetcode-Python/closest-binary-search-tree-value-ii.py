__author__ = 'Adward'
import bintree_utils


class Solution(object):
    def closestKValues(self, root, target, k):
        ans, stk1, stk2 = [], [], []

        def inorder(root, target, reverse, stack):  # reversed version will get predecessors
            if not root:
                return
            inorder(root.right if reverse else root.left, target, reverse, stack)
            if (reverse and root.val <= target) or (not reverse and root.val > target):
                return
            stack.append(root.val)
            inorder(root.left if reverse else root.right, target, reverse, stack)

        inorder(root, target, False, stk1)
        inorder(root, target, True, stk2)

        while k > 0:
            if len(stk1) == 0:
                ans.append(stk2.pop())
            elif len(stk2) == 0:
                ans.append(stk1.pop())
            elif abs(stk1[-1] - target) < abs(stk2[-1] - target):
                ans.append(stk1.pop())
            else:
                ans.append(stk2.pop())
            k -= 1
        return ans

    # deprecated
    def getPredecessor(self, node, fathers):
        tail = []
        if len(fathers) and node.val > fathers[-1].val:
            choice1 = fathers[-1]
            if node.left:
                tail.append(node)
                choice2 = node.left
                tail.append(choice2)
                while choice2.right:
                    choice2 = choice2.right
                    tail.append(choice2)
                if choice1.val > choice2.val:
                    fathers.pop()
                    return choice1
                else:
                    fathers += tail
                    fathers.pop()
                    return choice2
            else:
                fathers.pop()
                return choice1
        elif node.left:
            tail.append(node)
            choice2 = node.left
            tail.append(choice2)
            while choice2.right:
                choice2 = choice2.right
                tail.append(choice2)
            fathers += tail
            fathers.pop()
            return choice2
        else:
            try:
                p = fathers[-1]
            except:
                return None
            while len(fathers) > 1 and p.val > node.val:
                fathers.pop()
                p = fathers[-1]
            if len(fathers) and p.val < node.val:
                fathers.pop()
                return p
            else:
                return None

    def getSuccessor(self, node, fathers):
        tail = []
        if len(fathers) and node.val < fathers[-1].val:
            choice1 = fathers[-1]
            if node.right:
                tail.append(node)
                choice2 = node.right
                tail.append(choice2)
                while choice2.left:
                    choice2 = choice2.left
                    tail.append(choice2)
                if choice1.val < choice2.val:
                    fathers.pop()
                    return choice1
                else:
                    fathers += tail
                    fathers.pop()
                    return choice2
            else:
                fathers.pop()
                return choice1
        elif node.right:
            tail.append(node)
            choice2 = node.right
            tail.append(choice2)
            while choice2.left:
                choice2 = choice2.left
                tail.append(choice2)
            fathers += tail
            fathers.pop()
            return choice2
        else:
            try:
                p = fathers[-1]
            except:
                return None
            while len(fathers) > 1 and p.val < node.val:
                fathers.pop()
                p = fathers[-1]
            if len(fathers) and p.val > node.val:
                fathers.pop()
                return p
            else:
                return None

    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        p = root
        fathers = []
        while p.left or p.right:
            if target < p.val and p.left:
                fathers.append(p)
                p = p.left
            elif target > p.val and p.right:
                fathers.append(p)
                p = p.right
            else:
                break
        fathers.append(p)
        _fathers = [abs(p.val-target) for p in fathers]
        min_index = _fathers.index(min(_fathers))
        node = fathers[min_index]
        fathers_pre = fathers[0:min_index]
        fathers_suc = fathers[0:min_index]

        kVals = [node.val]
        cntdown = k - 1
        if cntdown == 0:
            return kVals
        preNode = self.getPredecessor(node, fathers_pre)
        sucNode = self.getSuccessor(node, fathers_suc)
        while cntdown:
            try:
                while cntdown and abs(preNode.val - target) < abs(sucNode.val - target):
                    kVals.append(preNode.val)
                    cntdown -= 1
                    preNode = self.getPredecessor(preNode, fathers_pre)

                # use >= instead of < to solve the dilemma when the suc and pre has same distance to target
                while cntdown and abs(preNode.val - target) >= abs(sucNode.val - target):
                    kVals.append(sucNode.val)
                    cntdown -= 1
                    sucNode = self.getSuccessor(sucNode, fathers_suc)
            except:
                if not preNode:
                    while cntdown:
                        kVals.append(sucNode.val)
                        cntdown -= 1
                        sucNode = self.getSuccessor(sucNode, fathers_suc)
                else:
                    while cntdown:
                        kVals.append(preNode.val)
                        cntdown -= 1
                        preNode = self.getPredecessor(preNode, fathers_pre)

        return kVals


sol = Solution()
codec = bintree_utils.Codec()
# treestr = '{5,3,6,2,4,#,#,1}'
# treestr = '{5,3,6,1,4,#,#,#,2}'
treestr = '{3,2,4,1}'
root = codec.deserialize(treestr)
print(sol.closestKValues(root, 2.0000, 3))