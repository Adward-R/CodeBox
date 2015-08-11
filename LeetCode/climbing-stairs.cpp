//
//  main.cpp
//  climbing-stairs
//
//  Created by Adward on 15/8/11.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        vector<int> vec = {1,2};
        for (int i=2; i<n; i++) {
            vec.push_back(vec[i-2] + vec[i-1]);
        }
        return vec[n-1];
    }
};
