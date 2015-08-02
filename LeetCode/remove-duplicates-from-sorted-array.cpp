//
//  main.cpp
//  remove-duplicates-from-sorted-array
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0) {
            return 0;
        }
        int len = 1;
        int n = nums[0];
        for (int i=1; i<nums.size(); i++) {
            if (nums[i] > n) { //new distinct number
                int tmp = nums[i];
                nums[i] = nums[len];
                nums[len] = tmp;
                n = tmp;
                len++;
            }
        }
        return len;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {1,1,2,2,2,3,3,4,5,5,5,5};
    cout << "len: " << sol.removeDuplicates(nums) << endl;
    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << ", ";
    }
    return 0;
}
