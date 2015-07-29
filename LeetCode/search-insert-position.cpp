//
//  main.cpp
//  search-insert-position
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (nums.size()==0) {
            return 0;
        }
        for (int i=0; i<nums.size(); i++) {
            if (nums[i]>=target) {
                return i;
            }
        }
        return nums.size();
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {1,3,5,6};
    cout << sol.searchInsert(nums, 0);
    return 0;
}
