//
//  main.cpp
//  rotate-image
//
//  Created by Adward on 15/7/19.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (&matrix==NULL || matrix.size()==0) {
            return;
        }
        int N = matrix.size();
        for (int i=0; i<N/2; i++) {
            for (int j=i; j<N-i-1; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[N-1-j][i];
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j];
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i];
                matrix[j][N-1-i] = tmp;
            }
        }
    }
};

int main(int argc, const char * argv[]) {
    vector<vector<int>> matrix = {
        {1,2},
        {3,4}
    };
    Solution sol;
    sol.rotate(matrix);
    int N = matrix.size();
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
