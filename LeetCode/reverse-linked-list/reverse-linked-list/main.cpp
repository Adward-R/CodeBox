//
//  main.cpp
//  reverse-linked-list
//
//  Created by Adward on 15/5/15.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution_iterative {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* p1 = head;
        if (p1 == NULL) { //empty list
            return NULL;
        }
        else {
            ListNode* p2 = p1->next;
            if (p2 == NULL) { //one-element list
                return head;
            }
            else { //normal list
                ListNode* p3 = p2->next;
                p1->next = NULL;
                p2->next = p1;
                while (p3 != NULL) {
                    p1 = p2;
                    p2 = p3;
                    p3 = p3->next;
                    p2->next = p1;
                }
                return p2;
            }
        }
    }
};

class Solution_recursive {
public:
    ListNode* reverse(ListNode* head){
        if (head->next != NULL) {
            ListNode* result = reverse(head->next);
            head->next->next = head;
            return result;
        }
        else {
            return head;
        }
    }
    ListNode* reverseList(ListNode* head){
        if (head != NULL){
            ListNode* result = reverse(head);
            head->next = NULL;
            return result;
        }
        else{
            return NULL;
        }
    }
};

class ListUtil {
private:
    ListNode* head;
public:
    ListNode* getHead(){
        return head;
    }
    void setHead(ListNode* head){
        this->head = head;
    }
    void buildList(int val[], int length){
        head = new ListNode(val[0]);
        ListNode* p = head;
        for (int i=1; i<length; i++) {
            p->next = new ListNode(val[i]);
            p = p->next;
        }
    }
    void printList(ListNode* head){
        ListNode* p = head;
        while (p != NULL) {
            cout<<(p->val)<<endl;
            p = p->next;
        }
    }
};


int main(int argc, const char * argv[]) {
    int list_val[] = {};
    ListUtil* listUtil = new ListUtil();
//    Solution_iterative* sol_ite= new Solution_iterative();
    Solution_recursive* sol_rec = new Solution_recursive();
    
    listUtil->buildList(list_val, 0);
//    listUtil->setHead(sol_ite->reverseList(listUtil->getHead()));
    listUtil->setHead(sol_rec->reverseList(listUtil->getHead()));
    listUtil->printList(listUtil->getHead());
    return 0;
}
