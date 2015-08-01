//
//  main.cpp
//  palindrome-number
//
//  Created by Adward on 15/8/1.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long xx = x; //x = -x may cause overflow! (when INT32_MIN is processed)
        long result = 0;
        bool isNegative = false;
        
        if (xx < 0) {
            isNegative = true;
            xx = -xx;
        }
        while (xx) {
            result = result * 10 + xx % 10;
            xx /= 10;
        }
        
        //test if exceeds int range
        if (isNegative) {
            if (-result < INT32_MIN) {
                //result > (-INT32_MIN) is wrong!!!
                //cuz -INT32_MIN  = INT32_MAX+1, will surely overflow
                //and become INT32_MIN again...interesting
                return 0;
            }
        }
        else {
            if (result > INT32_MAX) {
                return 0;
            }
        }
        return (isNegative ? -1 : 1) * int(result);
    }
    
    bool isPalindrome(int x) {
        if (x==0) {
            return true;
        }
        else if (x<0) {
            return false;
        }
        
//        cout << x << "|" << reverse(x) << endl;
        if (x==reverse(x)) {
            //if reversed x overflow, reverse(x) returns 0
            return true;
        }
        else {
            return false;
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.isPalindrome(-2147447412) << endl;
    return 0;
}
