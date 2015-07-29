//
//  main.cpp
//  number-of-1-bits
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        for (int i=0; i<32; i++) {
            cnt += n%2;
            n /= 2;
        }
        return cnt;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.hammingWeight(11);
    return 0;
}
