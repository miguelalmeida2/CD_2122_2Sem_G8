include <stdio.h>
include <stdlib.h>

int count_ones( int val ){
    int cnt = 0;
    for (int i = 0; i < sizeof(int); i++){
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
    printf("nBits = %d", res);
    sut = 32;
    res = count_ones(sut);
    printf("nBits = %d", res);
    sut = 1152;
    res = count_ones(sut);
    printf("nBits = %d", res);

}