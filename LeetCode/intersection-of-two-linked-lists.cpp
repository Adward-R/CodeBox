//
//  main.cpp
//  intersection-of-two-linked-lists
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    
    ListNode* lstConstruct(vector<int>& elements) {
        ListNode* l;
        if (elements.size()==0) {
            return NULL;
        }
        l = new ListNode(elements[0]);
        ListNode* ptr = l;
        for (int i=1; i<elements.size(); i++) {
            ptr->next = new ListNode(elements[i]);
            ptr = ptr->next;
        }
        return l;
    }
    void lstConcat(ListNode* l1, ListNode* l2) {
        if (!l1 || !l2) {
            return;
        }
        ListNode* ptr = l1;
        while (ptr->next) {
            ptr = ptr->next;
        }
        ptr->next = l2;
    }
    void lstDisplay(ListNode* head) {
        if (!head) {
            cout << "empty" << endl;
            return;
        }
        cout << head->val;
        ListNode* ptr = head->next;
        while (ptr) {
            cout << "->" << ptr->val;
            ptr = ptr->next;
        }
    }
    
    int lstLength(ListNode* head) {
        if (!head) {
            return 0;
        }
        int cnt = 1;
        ListNode* ptr = head->next;
        while (ptr) {
            cnt++;
            ptr = ptr->next;
        }
        return cnt;

    }
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenDiff = lstLength(headA) - lstLength(headB);
        for (int i=0; i<abs(lenDiff); i++) {
            if (lenDiff>0) {
                headA = headA->next;
            } else {
                headB = headB->next;
            }
        }
        while (headA && headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> param1 = {1,2};
    vector<int> param2 = {3,4,5};
    vector<int> param3 = {6,7,8};
    
    ListNode* l1 = sol.lstConstruct(param1);
    ListNode* l2 = sol.lstConstruct(param2);
    ListNode* l3 = sol.lstConstruct(param3);
    
//    sol.lstConcat(l1, l3);
    sol.lstConcat(l2, l3);
    
    ListNode* node = sol.getIntersectionNode(l1, l2);
    if (node) {
        cout << node->val;
    } else {
        cout << "null";
    }
    
    return 0;
}
