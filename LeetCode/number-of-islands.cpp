//
//  main.cpp
//  number-of-islands
//
//  Created by Adward on 15/7/29.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    void probing(int tmp, int& block, vector<vector<int>>& labels) {
        if (tmp > 1) { //probed labeled land
            if (block > 1) { //the block is already labeled
                if (tmp != block) {
                    //connects 2 labeled parts
                    vector<vector<int>>::iterator iit1, iit2, iit;
                    vector<int>::iterator it;
                    for (iit=labels.begin(); iit!=labels.end(); iit++) {
                        for (it=iit->begin(); it!=iit->end(); it++) {
                            if (*it == block) {
                                iit1 = iit;
                            }
                            else if (*it == tmp) {
                                iit2 = iit;
                            }
                        }
                    }
                    if (iit1 != iit2) { //if were not connected before
                        for (it=iit2->begin(); it!=iit2->end(); it++) {
                            iit1->push_back(*it);
                        }
                        labels.erase(iit2);
                    }
                }
            }
            else {
                block = tmp;
            }
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<int>> newgrid;
        for (int i=0; i<grid.size(); i++) {
            vector<int> tmpVec;
            for (int j=0; j<grid[i].size(); j++) {
                tmpVec.push_back(grid[i][j] - '0');
            }
            newgrid.push_back(tmpVec);
        }
        //converted input to int form so that
        // there will not occur char overflow when labeling
        
        //each line contains labels that are equivalent to the same known island
        vector<vector<int>> labels;
        int cntLabel = 2; //labeling start from 2
        int tmp;
        for (int i=0; i<newgrid.size(); i++) {
            for (int j=0; j<newgrid[i].size(); j++) {
                if (newgrid[i][j] == 1) { //if the block itself is part of land
                    //test if it is adjacent to any labeled part of land
                    if (i > 0) {
                        tmp = newgrid[i-1][j];
                        probing(tmp, newgrid[i][j], labels);
                    }
                    if (j > 0) {
                        tmp = newgrid[i][j-1];
                        probing(tmp, newgrid[i][j], labels);
                    }
                    
                    if (newgrid[i][j] == 1) { //starts a (probable) new island
                        newgrid[i][j] = cntLabel;
                        labels.push_back(*new vector<int>(1, cntLabel));
                        cntLabel ++;
                    }
                }
            }
        }
        /*
         cout << "labels:" << endl;
         for (int i=0; i<labels.size(); i++) {
         cout << labels[i][0];
         for (int j=1; j<labels[i].size(); j++) {
         cout << "->" << labels[i][j];
         }
         cout << endl;
         }
         cout << "___" << endl;
         */
        return labels.size();
    }
};

int main(int argc, const char * argv[]) {
    vector<vector<char>> grid = {
        {'0','0','0','0','0','0'},
        {'1','1','1','1','1','0'},
        {'0','0','0','1','0','0'},
        {'0','1','1','1','1','1'},
        {'0','0','0','0','0','0'},
        {'1','1','1','1','1','0'}
    };
    
    Solution sol;
    cout << sol.numIslands(grid) << endl;
    cout << "___" << endl;
    for (int i=0; i<grid.size(); i++) {
        for (int j=0; j<grid[i].size(); j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}
