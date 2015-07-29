//
//  main.cpp
//  factorial-trailing-zeroes
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
class Solution {
public:
    int trailingZeroes(int n) {
        //count of nums that <n and are times of 5, 25, 125, ...
        int pwr = 5;
        int sum = 0;
        while (pwr <= n/5) {
            //judging by "pwr <= n" is not okay,
            //cuz pwr will exceed the limit of integer
            //when n is very big
            sum += n/pwr;
            pwr *= 5;
        }
        sum += n/pwr; //for largest pwr
        return sum;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    std::cout << sol.trailingZeroes(2147483647);
    return 0;
}
