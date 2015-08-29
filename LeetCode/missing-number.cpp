//
//  main.cpp
//  missing-number
//
//  Created by Adward on 15/8/29.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        long sum = 0, sumMinus = 0;
        long len = nums.size();
        for (int i=0; i<len; i++) {
            sum += i;
            sumMinus += nums[i];
        }
        return int(len + sum - sumMinus);
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    /*
    long sum = 0;
    for (int i=0; i<INT32_MAX; i++) {
        sum += i;
        if (sum < 0) {
            cout << i;
            return 0;
        }
    }
    cout << sum;
     */
    //vector<int> nums = {1,0,3,4,7,5,6};
    vector<int> nums = {0};
    cout << sol.missingNumber(nums);
    return 0;
}
