//
//  main.cpp
//  remove-nth-node-from-end-of-list
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
    ListNode* l;
    
    void lstConstruct(vector<int>& elements) {
        if (elements.size()==0) {
            l = NULL;
            return;
        }
        l = new ListNode(elements[0]);
        ListNode* ptr = l;
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
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (!n) {
            return head;
        }
        ListNode* preDelPtr, *delPtr, *endPtr = head;
        for (int i=0; i<=n; i++) {
            if (endPtr) {
                endPtr = endPtr->next;
            } else {
                //del head
                preDelPtr = head->next;
                delete head;
                return preDelPtr;
            }
        }
        preDelPtr = head;
        delPtr = preDelPtr->next;
        
        while (endPtr) {
            preDelPtr = preDelPtr->next;
            delPtr = delPtr->next;
            endPtr = endPtr->next;
        }
        preDelPtr->next = delPtr->next;
        delete delPtr;
        return head;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> param = {1,2,3,4,5};
    sol.lstConstruct(param);
    sol.lstDisplay(sol.removeNthFromEnd(sol.l, 0));
    return 0;
}

