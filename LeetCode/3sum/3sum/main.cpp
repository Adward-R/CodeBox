//
//  main.cpp
//  3sum
//
//  Created by Adward on 15/8/1.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (!nums.size()) {
            return {{}};
        }
        vector<vector<int>> sss;
        set<vector<int>> ss;
        sort(nums.begin(), nums.end());
        vector<int>::iterator idxZero = lower_bound(nums.begin(), nums.end(), 0);
        vector<int>::iterator i,j,k;
        
        for (i=nums.begin(); i!=idxZero; ++i) {
            for (j=idxZero; j!=nums.end(); ++j) {
                int left = - (*i + *j);
                if (left>=0) {
                    if (binary_search(idxZero, j, left) || binary_search(j+1, nums.end(), left)) {
                        vector<int> tmp;
                        if (left >= *j) {
                            tmp = {*i, *j, left};
                        }
                        else {
                            tmp = {*i, left, *j};
                        }
                        ss.insert(tmp);
                    }
                }
                else {
                    if (binary_search(nums.begin(), i, left) || binary_search(i+1, idxZero, left)) {
                        vector<int> tmp;
                        if (left >= *i) {
                            tmp = {*i, left, *j};
                        }
                        else {
                            tmp = {left, *i, *j};
                        }
                        ss.insert(tmp);
                    }
                }
            }
        }
        
        set<vector<int>>::iterator it;
        for (it=ss.begin(); it!=ss.end(); ++it) {
            sss.push_back(*it);
        }
        return sss;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6};
    //vector<int> nums = {-1,0,1,2,-1,-4};
    vector<vector<int>> result = sol.threeSum(nums);
    for (int i=0; i<result.size(); i++) {
        cout << "(";
        for (int j=0; j<result[i].size(); j++) {
            cout << result[i][j] << ", ";
        }
        cout << ")" << endl;
    }
    return 0;
}
