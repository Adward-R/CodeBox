//
//  main.cpp
//  next-permutation
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
    bool nextPerInRange(vector<int>::iterator it1, vector<int>::iterator it2) {
        if (it2-it1==2) {
            if (*it1 < *(it1+1)) {
                int tmp = *it1;
                *it1 = *(it1+1);
                *(it1+1) = tmp;
                return true;
            } else {
                return false;
            }
        } else {
            if (nextPerInRange(it1+1, it2)) {
                return true;
            } else {
                if (*(it1+1) <= *it1) {
                    return false;
                } else {
                    sort(it1+1, it2);
                    for (vector<int>::iterator it=it1+1; it!=it2; ++it) {
                        if (*it > *it1) {
                            int tmp = *it;
                            *it = *it1;
                            *it1 = tmp;
                            break;
                        }
                    }
                    return true;
                }
            }
        }
    }
    void nextPermutation(vector<int>& nums) {
        if (nums.size()<2) {
            return;
        }
        if (!nextPerInRange(nums.begin(), nums.end())) {
            sort(nums.begin(), nums.end());
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {1,2,3,4};
    for (int j=0; j<24; j++) {
        sol.nextPermutation(nums);
        for (int i=0; i<nums.size(); i++) {
            cout << nums[i] << ",";
        }
        cout << endl;
    }
    return 0;
}
