//
//  main.cpp
//  divide-two-integers
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        bool minIntDivided = false; //indicates if divident==INT32_MIN
        //handle special cases or quick disposals
        if (divisor==0) {
            return INT32_MAX;
        } else if (dividend==0) {
            return 0;
        } else if (divisor==INT32_MIN) {
            if (dividend==INT32_MIN) {
                return 1;
            } else {
                return 0;
            }
        } else if (dividend==INT32_MIN) {
            if (divisor==-1) { //overflow!
                return INT32_MAX;
            } else if (divisor==1) {
                return INT32_MIN;
            } else {
                minIntDivided = true;
            }
        } else if (divisor==1) {
            return dividend;
        } else if (divisor==-1) {
            return -dividend;
        }
        
        bool isNegative = false;
        //adjust two operands to positive
        // while use -(INT32_MIN+divisor) trick to avoid overflow
        // the added divisor will be counted in final result
        if (dividend<0 && divisor<0) {
            divisor = -divisor;
            if (minIntDivided) {
                dividend += divisor;
            }
            dividend = -dividend;
        } else if (dividend>0 && divisor<0) {
            isNegative = true;
            divisor = -divisor;
        } else if (dividend<0 && divisor>0) {
            if (minIntDivided) {
                dividend += divisor;
            }
            dividend = -dividend;
            isNegative = true;
        }
        
        //quick disposal
        if (dividend < divisor) {
            return (minIntDivided ? (isNegative ? -1 : 1) : 0);
        }
        
        //adding powers of 2 to sum so that gradually get close to dividend
        // e.g. in case 200/2==100, 200 = (2<<6)*1 + (2<<5)*1 + (2<<2)*1
        // where "2" above is a divisor
        // so result = (1<<6)*1 + (1<<5)*1 + (1<<2)*1 = 100.
        int shift = 1;
        while (divisor<<shift <= dividend && divisor<<shift >= 0) {
            shift++;
        }
        int result = 1<<(--shift);
        int sum = divisor<<shift;
        shift -= 1;
        while (shift>=0) {
            int tmpsum = sum + (divisor<<shift);
            while (tmpsum<=dividend && tmpsum>=0) {
                sum = tmpsum;
                result += 1<<shift;
                tmpsum += (divisor<<shift);
            }
            shift--;
        }
        
        //count back the pre-added divisor
        if (minIntDivided) {
            result++;
        }
        return isNegative ? -result : result;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.divide(INT32_MIN,INT32_MAX);
    return 0;
}
