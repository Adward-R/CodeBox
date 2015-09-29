__author__ = 'Adward'
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

    res = []

    def pathSumRec(self, root, sum, path):
        """
        :type root: TreeNode
        :type sum: int
        :type path: List[int]
        :rtype: bool
        """
        currentVal = int(root.val)
        #print(currentVal)
        sum -= currentVal
        path.append(currentVal)

        if not root.left and not root.right and sum == 0:
            self.res.append([])
            for node in path:
                self.res[-1].append(node)
        if root.left:
            self.pathSumRec(root.left, sum, path)
        if root.right:
            self.pathSumRec(root.right, sum, path)

        sum += currentVal
        path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        self.pathSumRec(root, sum, [])
        return self.res

sol = Solution()
root = sol.binTreeBuild('{5,4,8,11,#,13,4,7,2,#,#,5,1}')
print(sol.pathSum(root, 22))