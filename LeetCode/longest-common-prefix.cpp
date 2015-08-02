//
//  main.cpp
//  longest-common-prefix
//
//  Created by Adward on 15/8/1.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (!strs.size()) {
            return "";
        }
        
        vector<int> lens;
        int min_len = INT32_MAX;
        for (int i=0; i<strs.size(); i++) {
            int len = strs[i].length();
            if (len < min_len) {
                min_len = len;
            }
            lens.push_back(len);
        }
        
        string prefix = "";
        try {
            for (int i=0; i<min_len; i++) {
                char ch = strs[0][i];
                for (int j=1; j<strs.size(); j++) {
                    if (strs[j][i]!=ch) {
                        throw "stop";
                    }
                }
                prefix += ch;
            }
        } catch (...) {}

        return prefix;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<string> strs = {};
    cout << sol.longestCommonPrefix(strs);
    return 0;
}
