//
//  main.cpp
//  count-and-say
//
//  Created by Adward on 15/8/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    string countAndSay(int n) {
        if (n==1) {
            return "1";
        } else if (n==2) {
            return "11";
        }
        string str = "11";
        string strBuilder;
        n -= 2;
        while (n) {
            char prevChar = str[0];
            int cnt = 1;
            strBuilder = "";
            for (int i=1; i<str.length(); i++) {
                if (str[i]==prevChar) {
                    cnt++;
                } else {
                    strBuilder += cnt + '0';
                    strBuilder += prevChar;
                    prevChar = str[i];
                    cnt = 1;
                }
            }
            strBuilder += cnt + '0';
            strBuilder += prevChar;
            str = strBuilder;
            n--;
        }
        return str;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    for (int i=1; i<=10; i++) {
        cout << sol.countAndSay(i) << endl;
    }
    return 0;
}
