//
//  MyEnigma.c
//
//  Created by Adward on 15/10/10.
//  Copyright (c) 2015 Eddie. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//rotors are set as 3-2-1 from left to right,
// and encryption is executed from right to left,
// thus the order is 1-2-3-3-2-1
char plugboard[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //no plugboard
char rotors[][27] = {
    "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "BDFHJLCPRTXVZNYEIWGAKMUSQO"
};
//expedite the reversed look-up of motors
char rotorsRev[][27] = {
    "UWYGADFPVZBECKMTHXSLRINQOJ",
    "AJPCZWRLFBDKOTYUQGENHXMIVS",
    "TAGBPCSDQEUFVNZHYIXJWLRKOM"
};
char reflector[27] = "YRUHQSLDPXNGOKMIEBFZCWVJAT";

//after execution, plainText->cipherText in place
void enigmaEncrypt(char ringSettings[4], char messageKeys[4], char* text) {
    char msgKeys[4];
    strcpy(msgKeys, messageKeys);
    int idx, delta, i;
    char ch;
    for (idx = 0; text[idx] != '\0'; idx ++) {
        //rotate
        msgKeys[0] = (msgKeys[0]-'A'+1) % 26 + 'A';
        if (msgKeys[0] == 'R' || msgKeys[1] == 'E') {
            msgKeys[1] = (msgKeys[1]-'A'+1) % 26 + 'A';
            if (msgKeys[1] == 'F') {
                msgKeys[2] = (msgKeys[2]-'A'+1) % 26 + 'A';
            }
        }
        //encrypt
        ch = text[idx];
        ch = plugboard[ch-'A'];
        //1->2->3
        for (i = 0; i <= 2; i ++) {
            delta = msgKeys[i] - ringSettings[i];
            ch = ((ch-'A') + delta + 26) % 26 + 'A';
            ch = rotors[i][ch-'A'];
            ch = ((ch-'A') - delta + 26) % 26 + 'A';
        }
        ch = reflector[ch-'A'];
        //3->2->1
        for (i = 2; i >= 0; i --) {
            delta = msgKeys[i] - ringSettings[i];
            ch = ((ch-'A') + delta + 26) % 26 + 'A';
            ch = rotorsRev[i][ch-'A'];
            ch = ((ch-'A') - delta + 26) % 26 + 'A';
        }
        ch = plugboard[ch-'A'];
        text[idx] = ch;
    }
}

int main(int argc, const char * argv[]) {
    char cypherText[17] = "EYGNPGDMFBMRYJKY";
    char plainText[17];
    char msgKeys[4];
    msgKeys[3] = '\0';
    int i, j, k, flag;
    
    flag = 0;
    for (i = 0; i < 26; i ++) {
        for (j = 0; j < 26; j ++) {
            for (k = 0; k < 26; k ++) {
                strcpy(plainText, cypherText);
                msgKeys[0] = 'A' + i;
                msgKeys[1] = 'A' + j;
                msgKeys[2] = 'A' + k;
                enigmaEncrypt("DAB", msgKeys, plainText);
                //printf("%s\n", plainText);
                if (strstr(plainText, "HITLER") != NULL) {
                    flag = 1;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }
        if (flag) {
            break;
        }
    }
    if (flag) {
        //MessageKeys in motor 1-2-3 order
        printf("MessageKeys=%c%c%c\n", 'A'+k, 'A'+j,'A'+i);
        printf("PlainText=%s\n", plainText);
    }
    return 0;
}
