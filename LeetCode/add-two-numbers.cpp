//
//  main.cpp
//  add-two-numbers
//
//  Created by Adward on 15/7/30.
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

ListNode* listConstruct(vector<int>& num) {
    //input in ordinary order, ourput in reversed order
    ListNode* lst = new ListNode(0);
    ListNode* p = lst;
    for (int i=num.size()-1; i>0; --i) {
        p->val = num[i];
        p->next = new ListNode(0);
        p = p->next;
    }
    p->val = num[0];
    p->next = 0;
    return lst;
}

void listDisplay(ListNode* lst) {
    vector<int> vec;
    for (ListNode* p=lst; p; p=p->next) {
        vec.push_back(p->val);
    }
    while (!vec.empty()) {
        cout << vec.back();
        vec.pop_back();
    }
}

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sum = new ListNode(0);
        ListNode* p1 = l1, *p2 = l2, *ps = sum;
//        ListNode* firstZeroPos = NULL;
        int carry = 0;
        while (1) {
            int tmp = (p1 ? p1->val : 0) + (p2 ? p2->val : 0) + carry;
            carry = 0;
            if (tmp > 9) {
                carry = 1;
                tmp -= 10;
            }
            /*if (!tmp) {
                if (!firstZeroPos) {
                    firstZeroPos = ps;
                }
            }
            else {
                firstZeroPos = NULL;
            }
            */
            ps->val = tmp;
            
            //move to next digit
            if ( (!p1||!p1->next) && (!p2||!p2->next) ) {
                if (carry) {
                    ps->next = new ListNode(1);
                    break;
                }
                else {
                    ps->next = NULL;
                    break;
                }
            }
            else {
                p1 = (!p1) ? NULL : p1->next;
                p2 = (!p2) ? NULL : p2->next;
                ps->next = new ListNode(0);
                ps = ps->next;
            }
        }
        return sum;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> op1 = {5};
    vector<int> op2 = {5};
    ListNode* num1 = listConstruct(op1);
    ListNode* num2 = listConstruct(op2);
    ListNode* sum = sol.addTwoNumbers(num1, num2);
    listDisplay(sum);
    return 0;
}
