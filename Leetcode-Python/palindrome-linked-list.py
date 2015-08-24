__author__ = 'Adward'

# Definition for singly-linked list.
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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        p = head
        len = 1
        while p.next:
            len += 1
            p = p.next

        if len == 1:
            return True
        elif len <= 3:
            return (head.val == p.val)

        p = head
        for i in range(int(len/2) - 1):
            p = p.next
        head2 = p.next
        head1 = self.reverseList(head, p.next)
        if len % 2 == 1:
            head2 = head2.next

        #self.lstDisplay(head1)
        #print('---')
        #self.lstDisplay(head2)

        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        if (not head1) and (not head2):
            return True
        else:
            return False

    def reverseList(self, head, tail):
        p1 = head
        p2 = p1.next
        p3 = p2.next
        #last = p1
        #p1.next = tail
        p1.next = None
        p2.next = p1
        while p3 != tail:
            p1 = p2
            p2 = p3
            p3 = p3.next
            p2.next = p1
        return p2#, last #head, last of reversed list

sol = Solution()
lst = [1,1]
node = sol.lstConstruct(lst)
print(sol.isPalindrome(node))