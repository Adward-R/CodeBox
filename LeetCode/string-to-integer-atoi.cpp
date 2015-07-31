//
//  main.cpp
//  string-to-integer-atoi
//
//  Created by Adward on 15/7/31.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    int isError;
    Solution(): isError(0) {}
    int myAtoi(string str) {
        int halfMaxAbsolute = int(pow(2, sizeof(int)*8-1));
        int maxInt = halfMaxAbsolute - 1;
        int minInt = - halfMaxAbsolute;
        long result = 0;
        bool isNegative = false;
        int len_s = str.length();
        int idx = 0;
        
        if (!len_s) { //empty
            return 0;
        }
        //find the first non-whitespace
        while (str[idx]==' ' && idx<len_s) {
            idx++;
        }
        if (idx==len_s) { //all whitespaces
            return 0;
        }
        
        //judge the + or -
        if (str[idx]=='-') {
            isNegative = true;
            idx++;
        }
        else if (str[idx]=='+') {
            idx++;
        }
        else if (!isdigit(str[idx])) {
            return 0;
        }
        //can perform conversion
        int cnt_len = 0;
        for (; idx<len_s; ++idx) {
            if (cnt_len>11) {
                if (isNegative) {
                    return minInt;
                }
                else {
                    return maxInt;
                }
            }
            if (!isdigit(str[idx])) {
                break;
            }
            else {
                result = 10 * result + str[idx] - '0';
                cnt_len++;
            }
        }
        if (isNegative) {
            if (-result < minInt) {
                return minInt;
            }
            else {
                return int(-result);
            }
        }
        else {
            if (result > maxInt) {
                return maxInt;
            }
            else {
                return int(result);
            }
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    /*
    cout << sol.myAtoi("  3") << endl;
    cout << sol.myAtoi("") << endl;
    cout << sol.myAtoi("2137219832132137129837219372193") << endl;
    cout << sol.myAtoi("  ") << endl;
    cout << sol.myAtoi("-218312") << endl;
    cout << sol.myAtoi("-23213-2132") << endl;
    cout << sol.myAtoi("  +1dhsa1") << endl;
     */
    cout << sol.myAtoi("-1") << endl;
    return 0;
}
