#include <openssl/md5.h>
#include <openssl/sha.h>
#include <openssl/rsa.h>
#include <string.h>
#include <stdio.h>

#define N "FF807E694D915875B13F47ACDDA61CE11F62E034150F84660BF34026ABAF8C37"
#define E "010001"
#define D "45AEF3CB207EAD939BBDD87C8B0F0CFCC5A366A5AF2AC5FE1261D7547C625F51"

unsigned char plaintext[] = 
	   "01. A quick brown fox jumps over the lazy dog.\n" \
	   "02. A quick brown fox jumps over the lazy dog.\n" \
	   "03. A quick brown fox jumps over the lazy dog.\n";

void part1() {
	int ret;
    BIGNUM *bnn, *bne, *bnd;
    bnn = BN_new();
    bne = BN_new();
    bnd = BN_new();
    BN_hex2bn(&bnn, N);
    BN_hex2bn(&bne, E);
    BN_hex2bn(&bnd, D);
    RSA *r = RSA_new();
    r->n = bnn;
    r->e = bne;
    r->d = bnd;

	int plen = sizeof(plaintext);
	unsigned char ctx[142];
	unsigned char IV[] = "0123456789ABCDEFDEADBEEFBADBEAD!";
	unsigned char tmp_p[32], tmp_e[32], seg_p[32];
	int idx = 0, i;

	memcpy(tmp_e, IV, 32);
	while (idx + 32 < plen) {
		memcpy(seg_p, plaintext+idx, 32);
		for (i=0; i<32; i++) {
			tmp_p[i] = tmp_e[i] ^ seg_p[i];
		}
//		tmp_p = tmp_e ^ seg_p;
		RSA_public_encrypt(32, tmp_p, tmp_e, r, RSA_NO_PADDING);
		memcpy(ctx+idx, tmp_e, 32);
		idx += 32;
	}
	unsigned char tmp_e2[32];
	memset(seg_p, 0, 32);
	memcpy(seg_p, plaintext+idx, plen-idx);
	for (i=0; i<32; i++) {
		tmp_p[i] = tmp_e[i] ^ seg_p[i];
	}
	memcpy(tmp_p+plen-idx, tmp_e+plen-idx, 32-plen+idx);
	RSA_public_encrypt(32, tmp_p, tmp_e2, r, RSA_NO_PADDING);
	memcpy(ctx+idx, tmp_e, plen-idx);
	memcpy(ctx+idx-32, tmp_e2, 32);

	for (i=0;i<plen;i++) {
    	printf("%02X",ctx[i]);
    }
    printf("\n");


}

void part2() {
	
    MD5_CTX md5_ctx;
    unsigned char m1[16];
    int i = 0;

    memset(m1,0,sizeof(m1));
    MD5_Init(&md5_ctx);
    MD5_Update(&md5_ctx, plaintext, strlen(plaintext));
    MD5_Final(m1, &md5_ctx);
    printf("%s\n", "M1: ");
    for (i=0;i<16;i++) {
        printf("%02X",m1[i]);
    }
    printf("\n");

    SHA_CTX sha_ctx;
    unsigned char m2[20];
    memset(m2, 0, sizeof(m2));
    SHA_Init(&sha_ctx);
    SHA_Update(&sha_ctx, plaintext, strlen(plaintext));
    SHA_Final(m2, &sha_ctx);
    printf("%s\n", "M2: ");
    for (i=0;i<20;i++) {
    	printf("%02X",m2[i]);
    }
    printf("\n");

    //M1 and M2 generated
    unsigned char m[36];
    memset(m, 0, sizeof(m));
    memcpy(m, m1, sizeof(m1));
    memcpy(m+16, m2, sizeof(m2));
    printf("%s\n", "M: ");
    for (i=0;i<36;i++) {
    	printf("%02X",m[i]);
    }
    printf("\n");
    
    //M generated
    int ret;
    BIGNUM *bnn, *bne, *bnd;
    unsigned char e1[32];
    memset(e1, 0, sizeof(e1));

    bnn = BN_new();
    bne = BN_new();
    bnd = BN_new();
    BN_hex2bn(&bnn, N);
    BN_hex2bn(&bne, E);
    BN_hex2bn(&bnd, D);

    RSA *r = RSA_new();
    r->n = bnn;
    r->e = bne;
    r->d = bnd;

    ret = RSA_private_encrypt(32, m, e1, r, RSA_NO_PADDING);
    /*
    if (ret < 0) {
    	printf("Encrypt failed!!!\n");
    	return 1;
    }
    
    for (i=0; i<ret; i++) {
    	printf("%02X", e1[i]);
    }
    */
    unsigned char p2[32];
    memcpy(p2, m+4, 4);
    memcpy(p2+4, e1+4, 28);

    unsigned char mm[36];
    ret = RSA_private_encrypt(32, p2, mm, r, RSA_NO_PADDING);
    memcpy(mm+32, e1, 4);
    printf("%s\n", "M': ");
    for (i=0;i<36;i++) {
    	printf("%02X",mm[i]);
    }
    printf("\n");

    //start ECB decryption of M'
    ret = RSA_public_decrypt(32, mm, p2, r, RSA_NO_PADDING);
    /*for (i=0;i<32;i++) {
    	printf("%02X",p2[i]);
    }
    printf("\n");*/
    memcpy(e1, mm+32, 4);
    memcpy(e1+4, p2+4, 28);
    ret = RSA_public_decrypt(32, e1, m, r, RSA_NO_PADDING);
    memcpy(m+32, p2, 4);
    printf("%s\n", "M'->: ");
    for (i=0;i<36;i++) {
    	printf("%02X",m[i]);
    }
    printf("\n");
}

int main() {
	part1();
	printf("-------\n");
	part2();
	return 0;
}