__author__ = 'Adward'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binTreeBuild(nodesLst):
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

class Solution(object):
    def __init__(self):
        self.chgNode = []

    def getMaxMinNode(self, root): #from modified BST
        """
        :type root: TreeNode
        :rtype: tuple[TreeNode]
        """
        maxQ = [TreeNode(-(2**31)), root, TreeNode(-(2**31))]
        minQ = [TreeNode(2**31-1), root, TreeNode(2**31-1)]
        if root.left:
            maxQ[0], minQ[0] = self.getMaxMinNode(root.left)
        if root.right:
            maxQ[2], minQ[2] = self.getMaxMinNode(root.right)

        #print(str(maxQ[0].val) + '|' + str(root.val) + '|' + str(minQ[2].val))
        if maxQ[0].val < root.val < minQ[2].val: #normal
            pass
        elif minQ[2].val < root.val < maxQ[0].val:
            self.chgNode.append(maxQ[0])
            self.chgNode.append(minQ[2])
        else:
            self.chgNode.append(root)
            if root.val < maxQ[0].val:
                self.chgNode.append(maxQ[0])
                #self.chgNode.append(root)
            if root.val > minQ[2].val:
                self.chgNode.append(minQ[2])
                #self.chgNode.append(root)
        return max(maxQ, key=lambda x: x.val), min(minQ, key=lambda x: x.val)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.getMaxMinNode(root)
        tmp = self.chgNode[-2].val
        self.chgNode[-2].val = self.chgNode[-1].val
        self.chgNode[-1].val = tmp

sol = Solution()
#root = binTreeBuild('{7,5,8,3,6,#,12,1,4,#,#,10,13,9}')
#root = binTreeBuild('{7,5,8,3,6,#,12,2}')
root = binTreeBuild('{2,5,8,3,6,#,12,7}')
sol.recoverTree(root)