//
//  main.cpp
//  longest-palindromic-substring
//
//  Created by Adward on 15/8/1.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int longest_odd = 0, longest_even = 0; //substring's length / 2
        int idx_odd=0, idx_even=0;
        
        if (s.length()==0) {
            return "";
        }
        //odd length palindromes
        for (int i=1; i<s.length()-1; i++) {
            int j=1;
            for (; i>=j && i+j<s.length(); j++) {
                if (s[i-j]!=s[i+j]) {
                    break;
                }
            }
            if (j-1 > longest_odd) {
                longest_odd = j - 1;
                idx_odd = i;
            }
        }
        //even
        for (int i=1; i<s.length(); i++) {
            int j = 0;
            for (; i>=j+1 & i+j<s.length(); j++) {
                if (s[i-j-1]!=s[i+j]) {
                    break;
                }
            }
            if (j > longest_even) {
                longest_even = j;
                idx_even = i;
            }
        }
        //compare (odd*2+1) with (even*2)
        if (longest_odd < longest_even) {
            return s.substr(idx_even-longest_even, 2*longest_even);
        }
        else {
            return s.substr(idx_odd-longest_odd, 2*longest_odd+1);
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    cout << sol.longestPalindrome("abdqweabebebbbbbbbbbbbb");
    return 0;
}
