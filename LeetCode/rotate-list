/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) {
            return NULL;
        }
        ListNode *prevHead, *newHead, *prevTail, *tail;
        prevHead = newHead = prevTail = tail = head;
        int length = 0;
        while (tail) {
            tail = tail->next;
            length++;
        }
        if (length <= k) {
            k = k % length;
        }
        if (!k || length == 1) {
            return head;
        }
        
        tail = head;
        int cnt = 0;
        while (tail) {
            tail = tail->next;
            if (cnt >= 1) {
                prevTail = prevTail->next;
            }
            if (cnt >= k) {
                newHead = newHead->next;
            }
            if (cnt >= k+1) {
                prevHead = prevHead->next;
            }
            cnt++;
        }
        
        prevTail->next = head;
        prevHead->next = NULL;
        return newHead;
    }
};