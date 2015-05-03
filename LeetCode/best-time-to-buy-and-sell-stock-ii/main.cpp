//
//  main.cpp
//  best-time-to-buy-and-sell-stock-ii
//
//  Created by Adward on 15/5/3.
//  Copyright (c) 2015年 Eddie. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2){
            return 0;
        }
        int profit = 0;
        int trend = (prices[1] - prices[0] > 0) ? 1 : 0; //1:up, 2:down
        
        if (prices.size() == 2){
            if (trend > 0){
                return prices[1] - prices[0];
            }
            else{
                return 0;
            }
        }
        
        int prev_extreme = 0;
        if (trend > 0){
            prev_extreme = prices[0];
        }
        int prev_price;// = prices[1];
        int pres_price = prices[1];
        for (vector<int>::iterator iter = prices.begin() + 2;
             iter != prices.end();++iter){
            prev_price = pres_price;
            pres_price = *iter;
            if (pres_price-prev_price >= 0 && trend > 0){
                ;
            }
            else if (pres_price-prev_price >= 0 && trend == 0){
                prev_extreme = prev_price;
                trend = 1;
            }
            else if (pres_price-prev_price < 0 && trend > 0){
                profit += (prev_price - prev_extreme);
                trend = 0;
            }
            else{
                ;
            }
        }
        
        if (trend > 0){
            profit += (pres_price - prev_extreme);
        }
        
        return profit;
    }
};

int main(int argc, const char * argv[]) {
    vector<int> prices;
    prices = {2,1};
    Solution sol;
    cout<<sol.maxProfit(prices)<<endl;
    return 0;
}
