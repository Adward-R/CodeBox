class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def buildLst(self, lst):
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        p = head
        for itm in lst[1:]:
            p.next = ListNode(itm)
            p = p.next
        return head

    def dispLst(self, head):
        p = head
        res = ''
        while p:
            res += str(p.val) + ', '
            p = p.next
        return res

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m >= n:
            return head
        p0 = head
        for i in range(m-2):
            p0 = p0.next
        if m == 1:
            p1 = p0
        else:
            p1 = p0.next
        p2 = p1.next
        p3 = p2.next

        for i in range(n-m):
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3:
                p3 = p3.next

        if m == 1:
            p0.next = p2
            return p1
        else:
            p0.next.next = p2
            p0.next = p1
            return head


sol = Solution()
head = sol.buildLst([1])
head = sol.reverseBetween(head,1,1)
print(sol.dispLst(head))