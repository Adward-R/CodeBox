//
//  main.cpp
//  remove-element
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int lenDiff = 0;
        int size = int(nums.size());
        int swpIdx = size-1;
        int i = 0;
        
        while (i + lenDiff < size) {
            if (val==nums[i]) {
                lenDiff++;
                while (swpIdx > i && nums[swpIdx] == val) {
                    lenDiff++;
                    swpIdx--;
                }
                if (swpIdx==i) { //all discarded
                    return i;
                }
                nums[i] = nums[swpIdx];
                nums[swpIdx] = val;
                swpIdx--;
            }
            i++;
        }
        return size-lenDiff;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {4};
    cout << "len: " << sol.removeElement(nums, 4) << endl;
    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << ", ";
    }
    return 0;
}
