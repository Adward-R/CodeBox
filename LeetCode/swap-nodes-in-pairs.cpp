//
//  main.cpp
//  swap-nodes-in-pairs
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
    
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        ListNode *even = head, *odd = head->next;
        head = odd;
        int status;
        ListNode* nextpair;
        
        do {
            status = 0;  //nextpair=odd->next == NULL, last pair and even length
            nextpair = odd->next;
            if (nextpair) {
                if (nextpair->next) {
                    status = 2; //next pair still exists, normal case
                    nextpair = nextpair->next;
                } else {
                    status = 1; //one more node but not a pair, odd length
                }
            }
            
            if (status==0) {
                even->next = NULL;
                odd->next = even;
            } else if (status==1) {
                even->next = nextpair;
                odd->next = even;
            } else {
                even->next = nextpair;
                ListNode* tmp = odd->next;
                odd->next = even;
                even = tmp;
                odd = nextpair; //or even->next
            }
        } while (status==2);
        
        return head;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> param = {1,2,3,4,5};
    
    ListNode* l = sol.lstConstruct(param);
    ListNode* node = sol.swapPairs(l);
    sol.lstDisplay(node);
    
    return 0;
}
