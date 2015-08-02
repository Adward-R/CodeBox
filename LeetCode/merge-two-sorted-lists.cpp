//
//  main.cpp
//  merge-two-sorted-lists
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
    ListNode* l[2];
    
    void lstConstruct(int idx, vector<int>& elements) {
        if (elements.size()==0) {
            l[idx] = NULL;
            return;
        }
        l[idx] = new ListNode(elements[0]);
        ListNode* ptr = l[idx];
        for (int i=1; i<elements.size(); i++) {
            ptr->next = new ListNode(elements[i]);
            ptr = ptr->next;
        }
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
    //linked-lists in increasing order
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (!l1) {
            return l2;
        } else if (!l2) {
            return l1;
        }
        
        ListNode* head, *now;
        ListNode* ptr[2];
        ptr[0] = l1;
        ptr[1] = l2;
        if (l1->val <= l2->val) {
            head = now = l1;
            ptr[0] = ptr[0]->next;
            
        } else {
            head = now = l2;
            ptr[1] = ptr[1]->next;
        }
        
        while (ptr[0] && ptr[1]) {
            int smaller = (ptr[0]->val <= ptr[1]->val) ? 0 : 1;
            now->next = ptr[smaller];
            now = now->next;
            ptr[smaller] = ptr[smaller]->next;
            
        }
        int not_end = ptr[0] ? 0 : 1;
        now->next = ptr[not_end];
        
        return head;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> param1 = {1,9};
    vector<int> param2 = {4,5,6};
    sol.lstConstruct(0, param1);
    sol.lstConstruct(1, param2);
    sol.lstDisplay(sol.mergeTwoLists(sol.l[0], sol.l[1]));
    return 0;
}
