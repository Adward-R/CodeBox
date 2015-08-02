//
//  main.cpp
//  implement-strstr
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        //haystack.length() - needle.length() will cause the overflow of unsigned
        long len1 = haystack.length();
        long len2 = needle.length();
        if (len1 < len2) {
            return -1;
        }
        for (int i=0; i<=len1-len2; i++) {
            bool found = true;
            for (int j=0; j<len2; j++) {
                if (haystack[i+j]!=needle[j]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                return i;
            }
        }
        return -1;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.strStr("21333", "213");
    return 0;
}
