__author__ = 'Adward'

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def buildList(self, lst):
        head = ListNode(lst[0])
        p = head
        for value in lst[1:]:
            p.next = ListNode(value)
            p = p.next
        return head

    def buildCycle(self, lst, idx):
        head = ListNode(lst[0])
        p = head
        for value in lst[1:]:
            p.next = ListNode(value)
            p = p.next
        q = head
        for i in range(idx):
            q = q.next
        p.next = q
        return head

    def dispList(self, head):
        cnt = 0
        while head and cnt <= 10:
            print(head.val)
            head = head.next
            cnt += 1

    def reverseList(self, head):
        p1 = head
        if p1 is None:
            return None
        else:
            p2 = p1.next
            if p2 is None:
                return head
            else:
                p3 = p2.next
                p1.next = None
                p2.next = p1
                while p3:
                    p1 = p2
                    p2 = p3
                    p3 = p3.next
                    p2.next = p1
                return p2

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        elif head.next is None:
            return False
        elif head.next == head:
            return True

        rhead = self.reverseList(head)
        if head.val == rhead.val:
            return True
        else:
            return False

sol = Solution()
lst = [1,2,3,4,5]
head = sol.buildList(lst)
print(sol.hasCycle(head))
#sol.dispList(head)
