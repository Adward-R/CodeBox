//
//  main.cpp
//  permutations
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
    vector<vector<int> > permute(vector<int>& nums) {
        vector<vector<int> > v;
        int n = 1;
        for (int i = 2; i <= nums.size(); ++i) {
            n *= i;
        }
        for (int i = 0; i < n; ++i) {
            v.push_back(nums);
            nextPermutation(nums);
        }
        return v;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {1,2,3,4};
    vector<vector<int> > v = sol.permute(nums);
    for (int j=0; j<v.size(); j++) {
        for (int i=0; i<v[j].size(); i++) {
            cout << v[j][i] << ",";
        }
        cout << endl;
    }
    return 0;
}
