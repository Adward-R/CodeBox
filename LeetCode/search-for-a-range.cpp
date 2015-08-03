//
//  main.cpp
//  search-for-a-range
//
//  Created by Adward on 15/8/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result;
        if (binary_search(nums.begin(), nums.end(), target)) {
            result.push_back(lower_bound(nums.begin(), nums.end(), target) - nums.begin());
            result.push_back(upper_bound(nums.begin(), nums.end(), target) - nums.begin()-1);
        } else {
            result = {-1,-1};
        }
        return result;
    }
    
    vector<int> searchRange2(vector<int>& nums, int target) {
        int begin = 0, end = nums.size()-1;
        int mid = (begin + end) / 2;
        vector<int> result = {-1,-1};
        
        while (end - begin > 1) {
            if (target <= nums[mid]) {
                end = mid;
            } else {
                begin = mid;
            }
            mid = (begin + end) / 2;
        }
        if (nums[begin] == target) {
            result[0] = begin;
        } else if (nums[end] == target) {
            result[0] = end;
        }
        
        begin = 0;
        end = nums.size()-1;
        mid = (begin + end) / 2;
        while (end - begin > 1) {
            if (target < nums[mid]) {
                end = mid;
            } else {
                begin = mid;
            }
            mid = (begin + end) / 2;
        }
        if (nums[end] == target) {
            result[1] = end;
        } else if (nums[begin] == target) {
            result[1] = begin;
        }
        
        return result;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {8,9,9,9,9,10};
    vector<int> result = sol.searchRange2(nums, 9);
    cout << "[" << result[0] << "," << result[1] << "]" << endl;
    return 0;
}
