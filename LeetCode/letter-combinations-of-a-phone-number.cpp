//
//  main.cpp
//  letter-combinations-of-a-phone-number
//
//  Created by Adward on 15/8/11.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (!digits.size()) {
            return {};
        }
        vector<string> alphabets;
        vector<string> vec;
        for (int i=0; i<digits.length(); i++) {
            switch (digits[i]) {
                case '2':
                    alphabets.push_back("abc");
                    break;
                case '3':
                    alphabets.push_back("def");
                    break;
                case '4':
                    alphabets.push_back("ghi");
                    break;
                case '5':
                    alphabets.push_back("jkl");
                    break;
                case '6':
                    alphabets.push_back("mno");
                    break;
                case '7':
                    alphabets.push_back("pqrs");
                    break;
                case '8':
                    alphabets.push_back("tuv");
                    break;
                case '9':
                    alphabets.push_back("wxyz");
                    break;
                default:
                    break;
            }
        }
        
        int asize = alphabets.size();
        int ptrs[asize];
        for (int i=0; i<asize; i++) {
            ptrs[i] = 0;
        }
        while (1) {
            string tmpStr = "";
            for (int i=0; i<asize; i++) {
                tmpStr += alphabets[i][ptrs[i]];
            }
            vec.push_back(tmpStr);
            //move ptrs to next combination
            int i = asize - 1;
            for (; i>=0; i--) {
                if (ptrs[i] == alphabets[i].size() - 1) {
                    ptrs[i] = 0;
                } else {
                    ptrs[i] += 1;
                    break;
                }
            }
            if (i < 0) {
                break;
            }
        }
        return vec;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<string> vec = sol.letterCombinations("23");
    for (int i=0; i<vec.size(); i++) {
        cout << vec[i] << ",";
    }
    return 0;
}
