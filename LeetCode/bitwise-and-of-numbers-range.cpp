#include <iostream>
#include <math.h>
using namespace std;

int rangeBitwiseAnd(int m, int n) {
    const int MAX_BIT_NUM = 31;

    if (m == n){
    	return m;
    }

   	int mbit[MAX_BIT_NUM], nbit[MAX_BIT_NUM];
    for (int i=0;i<MAX_BIT_NUM;i++){
    	mbit[i] = m % 2;
    	m /= 2;
    	nbit[i] = n % 2;
    	n /= 2;
    }

    int power = MAX_BIT_NUM - 1;
    int index_of_one[MAX_BIT_NUM];
    int ptr = 0, flag = 0;
    while (power>=0){
    	if (flag == 0 && nbit[power] == 0) {
    		power--;
    		continue;
    	}
    	else{
   			if (flag == 0){
    			flag = 1;
    		}
    		if (mbit[power] == 1 && nbit[power] == 1){
				index_of_one[ptr] = power;
				power--;
				ptr++;
    		}
    		else if (mbit[power] == 0 && nbit[power] == 0){
    			power--;
    		}
    		else {
    			break;
    		}
    	}
    }
 
   	int result = 0;
    if (ptr>0){
    	for (int j=0;j<ptr;j++){
    		result += pow(2, index_of_one[j]);
	    }
	}
    return result;
}

int main(){
    cout<<rangeBitwiseAnd(5,7)<<endl;
    return 0;
}