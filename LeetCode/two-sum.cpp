//
//  main.cpp
//  two-sum
//
//  Created by Adward on 15/7/29.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
private:
    static int comp(const int a, const int b) {
        return a<b;
    }
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result, tmpVec = nums;
        vector<int>::iterator it1, it2;
        
        sort(tmpVec.begin(), tmpVec.end(), comp);
        
        vector<int>::iterator lower, upper;
        lower = lower_bound(tmpVec.begin(), tmpVec.end(), target*1.0/2);
        upper = upper_bound(tmpVec.begin(), tmpVec.end(), target*1.0/2);
        cout << "lower: " << lower-tmpVec.begin() << "; upper: " << upper-tmpVec.begin() << endl;
        
        //exchange place of upper and lower will fail when duplicated nums exists
        for (it1 = tmpVec.begin(); it1 != upper; it1 ++) {
            for (it2 = lower; it2 != tmpVec.end(); it2 ++) {
                if (*it1 + *it2 == target) {
                    //go find idx in original vector "nums"
                    for (int i=0; i<nums.size(); i++) {
                        if (nums[i] == *it1 || nums[i] == *it2) {
                            result.push_back(i+1);
                        }
                    }
                    return result;
                }
            }
        }
        return {};
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {-1,-2,-3,-4,-5,0,0,9};
    vector<int> result = sol.twoSum(nums, -8);
    for (int i=0; i<result.size(); i++) {
        cout << result[i] << " ";
    }
    return 0;
}
