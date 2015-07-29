//
//  main.cpp
//  rotate-array
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int tmp, dst, src;
        int N = nums.size();
        if (N==0 || k==0 || k%N==0) {
            return;
        }
        while (N < k) {
            k -= N;
        }
        ////
        if ((N%k==0 || N%(N-k)==0) && k>1) {
            int rounds = (N%(N-k)==0) ? (N-k) : k;
            for (int i=0; i<rounds; i++) {
                tmp = nums[i];
                dst = i, src = N - k + i;
                do {
                    nums[dst] = nums[src];
                    dst = src;
                    src = (src-k<0) ? (N-k+src) : (src-k);
                } while (src!=i);
                nums[dst] = tmp;
            }
        }
        else {
            tmp = nums[0];
            dst = 0, src = N - k;
            do {
                nums[dst] = nums[src];
                dst = src;
                src = (src-k<0) ? (N-k+src) : (src-k);
            } while (src);
            nums[dst] = tmp;
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<int> nums = {1,2,3,4,5,6,7,8,9,10,11,12};
    sol.rotate(nums, 24);
    for (int i=0; i<nums.size(); i++) {
        cout << nums[i] << ",";
    }
    return 0;
}
