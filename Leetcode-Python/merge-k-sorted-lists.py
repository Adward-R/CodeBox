__author__ = 'Adward'
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def lstConstruct(self, lst):
        if len(lst)==0:
            return []
        head = ListNode(lst[0])
        ptr = head
        for i in range(1, len(lst)):
            ptr.next = ListNode(lst[i])
            ptr = ptr.next
        return head

    def lstDisplay(self, head):
        if not head:
            print("empty")
        while head:
            print(head.val)
            head = head.next

    def merge2Lists(self, head1, head2):
        """
        :type head1, head2: ListNode
        :rtype: ListNode
        """
        if not head1:
            return head2
        elif not head2:
            return head1

        nhead = head1
        if head1.val > head2.val:
            nhead = head2
            p1 = head1
            p2 = head2.next
        else:
            p1 = head1.next
            p2 = head2

        p = nhead
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next
        if p1:
            p.next = p1
        else:
            p.next = p2
        return nhead

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            mid = len(lists) // 2
            for i in range(mid):
                lists[i] = self.merge2Lists(lists[i], lists[-1])
                lists.pop()
        return lists[0]


sol = Solution()
nums = [
    [1,15],
    [2,3,11],
    [2,3,12],
    [7,7,7,7],
    [4,8,20]
]
lists = [sol.lstConstruct(num) for num in nums]
nhead = sol.mergeKLists(lists)
sol.lstDisplay(nhead)