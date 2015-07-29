//
//  main.cpp
//  largest-number
//
//  Created by Adward on 15/7/17.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class Solution {
public:
    static int comp(const int& a, const int& b) {
//        cout << (*a) << " vs " << *b <<endl;
        stringstream ss1, ss2;
        ss1 << a << b;
        ss2 << b << a;
        
        string s1 = ss1.str();
        string s2 = ss2.str();

        for (int i=0; i<s1.length(); i++) {
            if (s1[i] > s2[i]) {
                return 1;
            }
            else if (s1[i] < s2[i]) {
                return 0;
            }
        }
        return 0;
    }
    string largestNumber(vector<int>& nums) {
        stringstream result;
        if (nums.size()==0) {
            result << 0;
        }
        else {
            std::sort(nums.begin(), nums.end(), comp);
            if (nums[0]==0) {
                result << 0;
            }
            else {
                for (int i=0; i<nums.size(); i++) {
                    result << nums[i];
                }
            }
        }
        return result.str();
    }
};

int main(int argc, const char * argv[]) {
    vector<int> vec = {3, 30, 34, 5, 9};
    Solution sol;
    cout << sol.largestNumber(vec);
    return 0;
}
