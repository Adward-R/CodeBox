//
//  main.cpp
//  reverse-bits
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <cstdint>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t reversed = 0;
        for (int i=0; i<32; i++) {
            reversed = reversed * 2 + n%2;
            n /= 2;
        }
        return reversed;
    }
};

int main(int argc, const char * argv[]) {
    uint32_t n = 43261596;
    Solution sol;
    cout << sol.reverseBits(n);
    return 0;
}
