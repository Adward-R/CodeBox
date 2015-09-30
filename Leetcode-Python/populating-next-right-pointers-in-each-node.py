__author__ = 'Adward'
from copy import deepcopy
# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def binTreeBuild(self, nodesLst):
        """
        :type nodesLst: str
        :rtype: TreeNode
        """
        lst = nodesLst[1:-1].split(',')
        if (not lst[0].isdigit()) and (not lst[0][1:].isdigit()):
            return None
        head = TreeLinkNode(int(lst[0]))
        q = [head]
        onLeft = True
        for num in lst[1:]:
            if num.isdigit() or num[1:].isdigit():
                if onLeft:
                    q[0].left = TreeLinkNode(int(num))
                    onLeft = False
                    q.append(q[0].left)
                else:
                    q[0].right = TreeLinkNode(int(num))
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

    def getNode(self, root, bitstr):
        """
        :type root: TreeLinkNode
        :type bitstr: List[int]
        :rtype: TreeLinkNode
        """
        if bitstr is None:
            return None
        node = root
        for ch in bitstr:
            if ch == 0:
                node = node.left
            else:
                node = node.right
        return node

    def getNextBitstr(self, bitstr):
        """
        :type bitstr: List[int]
        :rtype: List[int]
        """
        leng = len(bitstr)
        if leng == 0:
            return None
        idx = leng - 1
        nextBitstr = deepcopy(bitstr)
        while nextBitstr[idx] == 1 and idx >= 0:
            nextBitstr[idx] = 0
            idx -= 1
        if idx < 0:
            return None
        else:
            nextBitstr[idx] = 1
        return nextBitstr

    def getAllBitstr(self, level):
        """
        :type level: int
        :rtype: List[str]
        """
        bitstrs = [[0]*level]
        theLast = bitstrs[0]
        while theLast:
            bitstrs.append(self.getNextBitstr(theLast))
            theLast = bitstrs[-1]
        return bitstrs

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # root is level 0
        depth = 0
        ptr = root
        if not ptr:
            return
        while ptr.left:
            depth += 1
            ptr = ptr.left

        for level in range(1, depth+1):
            nodes = [self.getNode(root, bitstr) for bitstr in self.getAllBitstr(level)]
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]

    def printLevel(self, root, level):
        nodes = []
        ptr = root
        for i in range(level):
            ptr = ptr.left
        while ptr:
            nodes.append(ptr.val)
            ptr = ptr.next
        return nodes

sol = Solution()
root = sol.binTreeBuild('{1,2,3,4,5,6,7}')
sol.connect(root)
print(sol.printLevel(root, 2))
