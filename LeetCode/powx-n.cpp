//
//  main.cpp
//  powx-n
//
//  Created by Adward on 15/8/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    bool floatEqual(double x, double y) {
        double z = x - y;
        double limit = 0.0000001;
        if (z > -limit && z < limit) {
            return true;
        } else {
            return false;
        }
    }
    double myPow(double x, int n) {
        if (floatEqual(x, 0.0)) {
            if (n > 0) {
                return 0;
            } else if (n < 0) {
                return -log(0); //inf
            } else {
                return 1; //pow(0,0)==1
            }
        } else if (x==0) {
            return 1;
        }
        
        bool isNegative = false;
        if (n < 0) {
            isNegative = true;
            n = -n;
        }
        
        double sum = 1, sum_n = 0, mul = x, mul_n = 1;
        while (sum_n < n) {
            while (sum_n + mul_n*2 <= n) {
                mul_n *= 2;
                mul *= mul;
            }
            sum_n += mul_n;
            sum *= mul;
            //
            mul_n = 1;
            mul = x;
        }
        
        return isNegative ? 1.0/sum : sum;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.myPow(0,0);
    return 0;
}
