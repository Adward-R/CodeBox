//
//  main.cpp
//  excel-sheet-column-number
//
//  Created by Adward on 15/8/11.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int idx = digits.size() - 1;
        if (digits[idx] < 9) {
            digits[idx]++;
            return digits;
        }
        
        int carry = 1;
        while (idx >= 0 && carry) {
            digits[idx] = (digits[idx] + 1) % 10;
            if (digits[idx]) {
                carry = 0;
            }
            idx--;
        }
        if (carry) {
            vector<int> vec;
            vec.push_back(1);
            for (int i=0; i<digits.size(); i++) {
                vec.push_back(0);
            }
            return vec;
        } else {
            return digits;
        }
    }
};
