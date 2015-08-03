//
//  main.cpp
//  valid-sudoku
//
//  Created by Adward on 15/8/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    const int SUDOKO_LEN = 9;
public:
    int isValidBlock(char ch) {
        if (ch >= '1' && ch <= '9') {
            return ch-'0';
        } else if (ch == '.') {
            return 0;
        } else {
            return -1;
        }
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        char ch;
        int num;
        //row validation
        // & structure integrity validation
        if (board.size() != SUDOKO_LEN) {
            return false;
        }

        for (int i=0; i<SUDOKO_LEN; i++) {
            if (board[i].size() != SUDOKO_LEN) {
                return false;
            }
            vector<bool> check(SUDOKO_LEN, false);
            for (int j=0; j<SUDOKO_LEN; j++) {
                ch = board[i][j];
                num = isValidBlock(ch);
                if (num == -1) {
                    return false;
                } else if (num == 0) {
                    continue;
                } else {
                    if (check[num-1]) {
                        return false;
                    } else {
                        check[num-1] = true;
                    }
                }
            }
        }

        //column validation
        for (int j=0; j<SUDOKO_LEN; j++) {
            vector<bool> check(SUDOKO_LEN, false);
            for (int i=0; i<SUDOKO_LEN; i++) {
                num = isValidBlock(board[i][j]);
                if (num) { //not empty
                    if (check[num-1]) {
                        return false;
                    } else {
                        check[num-1] = true;
                    }
                }
            }
        }
        
        //9-block validation
        for (int i=0; i<=6; i+=3) {
            for (int j=0; j<=6; j+=3) {
                vector<bool> check(SUDOKO_LEN, false);
                for (int k=0; k<3; k++) {
                    for (int l=0; l<3; l++) {
                        num = isValidBlock(board[i+k][j+l]);
                        if (num) {
                            if (check[num-1]) {
                                return false;
                            } else {
                                check[num-1] = true;
                            }
                        }
                    }
                }
            }
        }
        
        return true;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<vector<char>> board = {
        {'.','8','7','6','5','4','3','2','1'},
        {'2','.','.','.','.','.','.','.','.'},
        {'3','.','.','.','.','.','.','.','.'},
        {'4','.','.','.','.','.','.','.','.'},
        {'5','.','.','.','.','.','.','.','.'},
        {'6','.','.','.','.','.','.','.','.'},
        {'7','.','.','.','.','.','.','.','.'},
        {'8','.','.','.','.','.','.','.','.'},
        {'9','.','.','.','.','.','.','.','.'},
    };
    cout << sol.isValidSudoku(board);
    return 0;
}
