//
//  main.cpp
//  excel-sheet-column-number
//
//  Created by Adward on 15/8/11.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

class Solution {
public:
    int titleToNumber(string s) {
        int weight = 1;
        int num = 0;
        for (int i=s.length()-1; i>=0; i--) {
            num += weight * (s[i]-'A'+1);
            if (num < 0) return INT32_MAX;
            weight *= 26;
        }
        return num;
    }
};
