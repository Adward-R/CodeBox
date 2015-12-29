__author__ = 'Adward'

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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getNodeByPath(n1, leng, pathNum):
            stk = []
            for i in range(leng):
                stk.append(pathNum % 2)
                pathNum = int(pathNum/2)
            n2 = n1
            while len(stk):
                if not n2:
                    return None
                else:
                    if stk[-1]:
                        n2 = n2.right
                    else:
                        n2 = n2.left
                    stk.pop()
            return n2

        if not root:
            return 0
        h = -1
        p = root
        while p:
            p = p.left
            h += 1
        #print(h)
        left = 0
        right = 2 ** (h-1) - 1
        while left + 1 < right:
            mid = int((left+right)/2)
            node = getNodeByPath(root, h-1, mid)

            if node.right:
                left = mid
            elif node.left:
                return 2**h + 2*mid
            else:
                right = mid

        node1 = getNodeByPath(root, h-1, left)
        node2 = getNodeByPath(root, h-1, right)
        if node2.left:
            if node2.right:
                return 2**h + 2*right + 1
            else:
                return 2**h + 2*right
        else:
            if node1.right:
                return 2**h + 2*left + 1
            else:
                return 2**h + 2*left

sol = Solution()
root = binTreeBuild('{0}')
print(sol.countNodes(root))