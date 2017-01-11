__author__ = 'Adward'
class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        class Node(object):
            def __init__(self, val, parent):
                self.val, self.parent = val, parent
                self.left = self.right = None

        root = Node(expression[0], None)
        i = 2
        p = root
        while i < len(expression):
            ch = expression[i]
            newNode = Node(ch, p)
            if not p.left:
                p.left = newNode
            else:
                while p.right:
                    p = p.parent
                p.right = newNode
            if (ch == 'T' or ch == 'F') and i+1 < len(expression) and expression[i+1] == '?':
                p = newNode
            i += 2

        def evalTree(node):
            if not node.left and not node.right:
                return node.val
            if node.val == 'T':
                return evalTree(node.left)
            else:
                return evalTree(node.right)
        return evalTree(root)