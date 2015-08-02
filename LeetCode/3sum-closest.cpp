//
//  main.cpp
//  3sum-closest
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size()==0) {
            return 0;
        }
        int diff = INT32_MAX;
        sort(nums.begin(), nums.end());
        int min = nums.front();
        int max = nums.back();
        
        int minSum = min + *(nums.begin()+1) + *(nums.begin()+2);
        int maxSum = max + *(nums.end()-2) + *(nums.end()-3);
        if (target >= maxSum) {
            return maxSum;
        } else if (target <= minSum) {
            return minSum;
        }
        
        for (int i=0; i<nums.size()-2; i++) {
            for (int j=i+1; j<nums.size()-1; j++) {
                int left = target - nums[i] - nums[j];
                int low, high;
                
                if (left < nums[j]) {
                    continue;
                    //low = min;
                } else if (left > max) {
                    low = max;
                } else {
                    low = *lower_bound(nums.begin()+j+1, nums.end(), left);
                }

                if (low == left) {
//                    cout << i << " " << j << " " << left << " " << low << endl;
                    return target;
                } else {
                    if (left < min) {
                        continue;
                        //high = min;
                    } else if (left > max) {
                        high = max;
                    } else {
                        high = *upper_bound(nums.begin()+j+1, nums.end(), left);
                    }
                    
                    if (high-left > left-low) {
                        if (abs(diff)>abs(low-left)) {
                            diff = low-left;
                        }
                    } else {
                        if (abs(diff)>abs(left-high)) {
                            diff = high-left;
                        }
                    }
                }
            }
        }
        return target+diff;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {-10,0,-2,3,-8,1,-10,8,-8,6,-7,0,-7,2,2,-5,-8,1,-4,6};
    cout << sol.threeSumClosest(nums, 18);
    return 0;
}
