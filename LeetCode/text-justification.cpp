//
//  main.cpp
//  text-justification
//
//  Created by Adward on 15/7/17.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
private:
    int widthCnt; //the actual width of next line words (including spaces!)
    int getRange(vector<string>& words, int maxWidth, int ptr1) {
        //get the range of next line to be formatted
        //(from words[ptr1] to words[ptr2])
        //and store widthCnt
        int ptr2;
        widthCnt = words[ptr1].length();
        for (ptr2=ptr1+1; ptr2<words.size(); ptr2++) {
            //with the width of each space
            int tmpCnt = widthCnt + 1 + words[ptr2].length();
            if (tmpCnt > maxWidth) {
                ptr2--; //drawback
                //widthCnt -= ptr2 - ptr1;
                break;
            }
            else {
                widthCnt = tmpCnt;
            }
        }
        if (ptr2==words.size()) {
            ptr2--;
            //widthCnt -= ptr2 - ptr1;
        }
        return ptr2;
    }
public:
    //not considering the condition that a word's length is larger than maxWidth?
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> vec;
        int ptr1=0, ptr2;
        int i;
        
        while (1) {
            string s;
            ptr2 = getRange(words, maxWidth, ptr1);
            if (ptr2==words.size()-1) {
                //last line
                s = words[ptr1];
                for (i=ptr1+1; i<=ptr2; i++) {
                    s += " " + words[i];
                }
                for (i=0; i<maxWidth-widthCnt; i++) {
                    s += " ";
                }
                vec.push_back(s);
                break;
            }
            else if (ptr2==ptr1) {
                //not last line, but has merely one word
                s = words[ptr1];
                for (i=0; i<maxWidth-widthCnt; i++) {
                    s += " ";
                }
                vec.push_back(s);
                widthCnt = 0;
            }
            else {
                //ordinary case
                int basicSlotWidth = (maxWidth - widthCnt) / (ptr2 - ptr1) + 1;
                int extraSlotRange = (maxWidth - widthCnt) % (ptr2 - ptr1);
                string basicSlot;
                for (i=0; i<basicSlotWidth; i++) {
                    basicSlot += " ";
                }
                
                s = words[ptr1];
                for (i=ptr1+1; i<=ptr2; i++) {
                    if (i <= ptr1+extraSlotRange) {
                        s += " ";
                    }
                    s += basicSlot + words[i];
                }
                vec.push_back(s);
                widthCnt = 0;
            }
            ptr1 = ptr2 + 1;
        }
        return vec;
    }
};

int main(int argc, const char * argv[]) {
    Solution sol;
    vector<string> words = {"This", "is", "an", "example", "of", "text", "justification."};
    int L = 16;
    vector<string> lines = sol.fullJustify(words, L);
    for (int i=0; i<lines.size(); i++) {
        cout << lines[i] << endl;
    }
    return 0;
}
