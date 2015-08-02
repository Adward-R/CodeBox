//
//  main.cpp
//  generate-parentheses
//
//  Created by Adward on 15/8/2.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
private:
    vector<string> collection;
    void recursiveGen(int unpairedLeft, int usedLeft, int usedRight, int n, string str) {
        if (usedLeft == n && usedRight == n-1) {
            collection.push_back(str+")");
            //cout << str+")" << endl;
            return;
        } else if (usedLeft == n) {
            recursiveGen(unpairedLeft-1, n, usedRight+1, n, str+")");
        } else if (unpairedLeft == 0) {
            recursiveGen(1, usedLeft+1, usedRight, n, str+"(");
        } else {
            recursiveGen(unpairedLeft+1, usedLeft+1, usedRight, n, str+"(");
            recursiveGen(unpairedLeft-1, usedLeft, usedRight+1, n, str+")");
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        if (n==0) {
            return {};
        }
        recursiveGen(1, 1, 0, n, "("); //start with "(" or "Left"
        vector<string> result = collection;
        collection.clear();
        return result;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<string> result = sol.generateParenthesis(3);
    for (int i=0; i<result.size(); i++) {
        cout << result[i] << endl;
    }
    return 0;
}
