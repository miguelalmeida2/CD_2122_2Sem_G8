#include <stdio.h>
#include <stdlib.h>

int count_ones( int val ){
    int cnt = 0;
    // Hardcoded sizeof int due to bug in memory 
    for (int i = 0; i < 32; i++){
        if(val & 0x1){
            cnt++;
        }
        val = val >> 1;
    }
    return cnt;
}

int main(){
    int sut = 10;
    int res = count_ones(sut);
    printf("nBits = %d\n", res);
    sut = 32;
    res = count_ones(sut);
    printf("nBits = %d\n", res);
    sut = 1152;
    res = count_ones(sut);
    printf("nBits = %d\n", res);
}