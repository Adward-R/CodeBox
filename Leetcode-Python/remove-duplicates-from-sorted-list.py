__author__ = 'Adward'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        ptr1 = head
        ptr2 = head
        val = head.val
        while True:
            while ptr2 and ptr2.val == val:
                ptr2 = ptr2.next
            if not ptr2:
                ptr1.next = None
                break
            ptr1.next = ptr2
            val = ptr2.val
            ptr1 = ptr2
            ptr2 = ptr2.next
        return head
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

sol = Solution()
lst = []
node = sol.lstConstruct(lst)
node = sol.deleteDuplicates(node)
sol.lstDisplay(node)