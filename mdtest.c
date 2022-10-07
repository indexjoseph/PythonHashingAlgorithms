#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>

int main(int argc, char *argv[]){
    //uncomment the line below if running the OpenSSL  version 1.02 or less
    //OpenSSL_add_all_algorithms();
    
    EVP_MD_CTX *mdctx;
    const EVP_MD *md;
    char mess1[] = "Test Message\n";
    char mess2[] = "Hello World\n";
    unsigned char md_value[EVP_MAX_MD_SIZE];
    unsigned int md_len,i;

    if (argv[1] == NULL){
        printf("usage: mdtest digestname\n");
        exit(1);
    }

    md = EVP_get_digestbyname(argv[1]);
    
    if (md == NULL){
        printf("Unknown message diagest %s\n",argv[1]);
        exit(1);
    }

    mdctx = EVP_MD_CTX_new(_);
    EVP_DigestInit_ex(mdctx,md, NULL);
    EVP_DigestUpdate(mdctx, mess1, strlen(mess1) );
    EVP_DigestUpdate(mdctx, mess2, strlen(mess2) );
    EVP_DigestFinal_ex(mdctx, md_value,&md_len);
    EVP_MD_CTX_destroy(mdctx);

    printf("Digest is: ");
    for(i =0;i < md_len; i++)
        printf("%02x",md_value[i]);
    printf("\n");

    exit(0);
}