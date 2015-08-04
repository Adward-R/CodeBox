//
//  main.cpp
//  jump-game
//
//  Created by Adward on 15/8/4.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() <=1) {
            return true;
        } else if (nums[0] == 0) {
            return false;
        }
        for (int i=1; i<nums.size()-1; i++) {
            if (nums[i] == 0) {
                int idx = i - 1;
                int flag = 1;
                while (idx >= 0) {
                    if (nums[idx] > i - idx) {
                        flag = 0;
                        break;
                    }
                    idx --;
                }
                if (flag) {
                    return false;
                }
            }
        }
        return true;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {3,2,1,0,4};
    cout << sol.canJump(nums);
    return 0;
}
