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
        ptr1 = head
        if not ptr1:
            return []
        ptr2 = head.next
        if not ptr2:
            return head
        nodes = []
        dist = 1
        while ptr2:
            if ptr1.val == ptr2.val:
                while ptr2 and ptr1.val == ptr2.val:
                    ptr2 = ptr2.next
                    dist += 1
            else:
                nodes.append(ptr1)
            if not ptr2:
                break
            else:
                ptr1 = ptr2
                ptr2 = ptr1.next
                dist = 1
        if dist == 1:
            nodes.append(ptr1)
        #if len(nodes) == 0:
        #    return []
        nodes.append(None)

        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]

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
lst = [1,1]
node = sol.lstConstruct(lst)
node = sol.deleteDuplicates(node)
sol.lstDisplay(node)