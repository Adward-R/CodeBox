//
//  main.cpp
//  add-binary
//
//  Created by Adward on 15/8/10.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        long idx;
        //len of original strings must be saved before they are adjusted
        long a_len = a.length(), b_len = b.length();
        if (a_len != b_len) {
            bool aShorter = (a_len < b_len) ? true : false;
            if (aShorter) {
                for (int i=0; i<b_len - a_len; i++) {
                    a = '0' + a;
                }
                idx = b_len - 1;
            } else {
                for (int i=0; i<a_len - b_len; i++) {
                    b = '0' + b;
                }
                idx = a_len - 1;
            }
        } else {
            idx = a_len - 1;
        }
        
        int carry = 0;
        string c = "";
        
        while (idx >= 0) {
            c = char((a[idx]-'0')^(b[idx]-'0')^(carry) + '0') + c;
            carry = ((a[idx]-'0')&(b[idx]-'0')) | ((a[idx]-'0')&carry) | ((b[idx]-'0')&carry);
            idx--;
        }
        if (carry) {
            c = '1' + c;
        }
        int i = 0;
        long c_len = c.length();
        for (; i<c_len; i++) {
            if (c[i] == '1') {
                break;
            }
        }
        
        string c_subs = c.substr(i, c_len-i);
        if (c_subs == "") {
            return "0";
        } else {
            return c_subs;
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.addBinary("0", "00");
    return 0;
}
