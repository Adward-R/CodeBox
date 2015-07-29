//
//  main.cpp
//  spiral-matrix-ii
//
//  Created by Adward on 15/7/29.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> result;
        if (n<1) {
            return {};
        }
        //init matrix
        for (int i=0; i<n; i++) {
            vector<int> tmpVec;
            for (int j=0; j<n; j++) {
                tmpVec.push_back(0);
            }
            result.push_back(tmpVec);
        }
        //init direction
        int direction = 0;
        int x=0, y=0; //location
        for (int num=1; num<=n*n; num++) {
            result[x][y] = num;
            //to find next place
            switch (direction) {
                case 0: //right
                    if (y<n-1 && result[x][y+1]==0) {
                        y++;
                    }
                    else {
                        direction++;
                        x++;
                    }
                    break;
                case 1: //down
                    if (x<n-1 && result[x+1][y]==0) {
                        x++;
                    }
                    else {
                        direction++;
                        y--;
                    }
                    break;
                case 2: //left
                    if (y>0 && result[x][y-1]==0) {
                        y--;
                    }
                    else {
                        direction++;
                        x--;
                    }
                    break;
                case 3: //up
                    if (x>0 && result[x-1][y]==0) {
                        x--;
                    }
                    else {
                        direction=0;
                        y++;
                    }
                    break;
                default:
                    break;
            }
        }
        return result;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    int n = 1;
    vector<vector<int>> result = sol.generateMatrix(n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
