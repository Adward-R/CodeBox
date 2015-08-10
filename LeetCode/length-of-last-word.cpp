//
//  main.cpp
//  length-of-last-word
//
//  Created by Adward on 15/8/10.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.length() - 1;
        while (s[i] == ' ') {
            i--;
        }
        
        int cnt = 0;
        while (i >= 0) {
            if (s[i] == ' ') {
                break;
            }
            cnt++;
            i--;
        }
        return cnt;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    std::cout << sol.lengthOfLastWord("   ");
    return 0;
}
