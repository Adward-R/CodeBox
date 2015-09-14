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

    def binTreeSerial1(self, head): #level-order
        """
        :type head: TreeNode
        :rtype: str
        """
        res = '{'
        q = [head]
        while len(q) != 0:
            res += str(q[0].val) + ','
            if q[0].left:
                q.append(q[0].left)
            if q[0].right:
                q.append(q[0].right)
            q = q[1:]
        res = res[0:-1]
        res += '}'
        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        currentLevel = -1
        q = [(root, 0)]
        while len(q) != 0:
            if q[0][1] > currentLevel:
                currentLevel += 1
                res.append([])
            res[-1].append(int(q[0][0].val))
            if q[0][0].left:
                q.append((q[0][0].left, q[0][1]+1))
            if q[0][0].right:
                q.append((q[0][0].right, q[0][1]+1))
            q = q[1:]
        return res



sol = Solution()
head = sol.binTreeBuild("{3,9,20,#,#,15,7}")
print(sol.levelOrder(head))