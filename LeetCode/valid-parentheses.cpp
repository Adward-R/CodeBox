//
//  main.cpp
//  valid-parentheses
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    char pair(char right) {
        switch (right) {
            case ')':
                return '(';
            case ']':
                return '[';
            default:
                return '{';
        }
    }
public:
    bool isValid(string s) {
        vector<char> vec;
        for (int i=0; i<s.length(); i++) {
            if (s[i]=='(' || s[i]=='[' || s[i]=='{') {
                vec.push_back(s[i]);
            } else if (s[i]==')' || s[i]==']' || s[i]=='}') {
                if (vec.empty()) {
                    return false;
                } else {
                    if (vec.back()!=pair(s[i])) {
                        return false;
                    } else {
                        vec.pop_back();
                    }
                }
            } else {
                return  false;
            }
        }
        return vec.empty();
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.isValid("{}({[]})");
    return 0;
}
