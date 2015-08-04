//
//  main.cpp
//  maximum-subarray
//
//  Created by Adward on 15/8/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, maxSum = 0;
        int i = 0;
        int maxMinus = INT32_MIN;
        
        while (i < nums.size() && nums[i] < 0) {
            if (nums[i] > maxMinus) {
                maxMinus = nums[i];
            }
            i++;
        }
        if (i == nums.size()) {
            //all minus
            return maxMinus;
        }

        while (i < nums.size()) {
            int tmp = nums[i];
            sum += tmp;
            if (sum < 0) {
                sum = 0;
            } else if (sum > maxSum) {
                maxSum = sum;
            }
            i++;
        }
        
        return maxSum;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {0,-2,0};
    cout << sol.maxSubArray(nums);
    return 0;
}
