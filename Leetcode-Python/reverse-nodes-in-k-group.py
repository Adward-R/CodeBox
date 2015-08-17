__author__ = 'Adward'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
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

    def reverseList(self, head, tail):
        p1 = head
        p2 = p1.next
        p3 = p2.next
        last = p1
        p1.next = tail
        p2.next = p1
        while p3 != tail:
            p1 = p2
            p2 = p3
            p3 = p3.next
            p2.next = p1
        return p2, last #head, last of reversed list

    def reverseKGroup(self, head, k):
        if k <= 1 or not head:
            return head
        isFirst = 1
        p1 = head
        p2 = p1
        last = None
        while True:
            flag = 0
            for i in range(k):
                if p2:
                    p2 = p2.next
                else:
                    flag = 1
                    break
            if flag:
                flag = 0
                break
            else:
                if isFirst:
                    isFirst = 0
                    #last = head
                    head, last = self.reverseList(p1, p2)
                else:
                    last.next, last = self.reverseList(p1, p2)
                p1 = p2
        return head

sol = Solution()
lst = [1,2,3,4,5,6]
node = sol.lstConstruct(lst)
node = sol.reverseKGroup(node, 2)
sol.lstDisplay(node)