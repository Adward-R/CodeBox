#include <stdio.h>

void reverseWords(char *s) {
    int leftSft = 0;
    char tmp;
    int left, i, j;
    int numOfChars = 0;
    int numOfWords = 0;
    left = -1;

    for (i = 0; s[i] != '\0'; ++i) {
    	if (left < 0) {
    		if (s[i] != ' ') {
    			numOfChars += 1;
    			left = i;
    		} else {
    			leftSft += 1;
    		}
    	} else {    		
    		if (s[i] == ' ') {
    			numOfWords += 1;
    			for (j = left; j < i; ++j) {
    				s[j-leftSft] = s[j];
    			}
    			s[i-leftSft] = ' ';
    			left = -1;
    		} else {
    			numOfChars += 1;
    		}
    	}
    }
    if (left >= 0) {
    	numOfWords += 1;
    	for (j = left; j < i; ++j) {
    		s[j-leftSft] = s[j];
    	}
    	s[i-leftSft] = '\0';
    } else {
    	s[numOfChars+numOfWords-1] = '\0';
    }
    
    printf("%d %d\n", numOfWords, numOfChars);
    ////
    int leng = numOfChars+numOfWords-1;
    i = 0;
    j = leng - 1;
    while (i < j) {
    	tmp = s[i];
    	s[i] = s[j];
    	s[j] = tmp;
    	i += 1;
    	j -= 1;
    }
    ////
    int p1, p2;
    left = -1;
    s[leng] = ' ';
    for (i = 0; i <= leng; ++i)
    {
    	if (left < 0) {
    		if (s[i] != ' ') {
    			left = i;
    		}
    	} else {    		
    		if (s[i] == ' ') {
    			p1 = left;
    			p2 = i - 1;
    			while (p1 < p2) {
    				tmp = s[p1];
    				s[p1] = s[p2];
    				s[p2] = tmp;
    				p1 += 1;
    				p2 -= 1;
    			}
    			left = -1;
    		}
    	}
    }
    s[leng] = '\0';
}

int main() {
	char s[] = "";
//	char s[] = "  a bc  ";
	reverseWords(s);
	printf("%s\n", s);
	return 0;
}