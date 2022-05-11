#include <stdio.h>
#include <stdlib.h>

 void print_bits( int array[], size_t array_size )
{
    int val = 0;
    for(int i = 0; i< array_size; i++){
        val = array[i];
        printf("Val = %d , bin = ",val);
        for(int j = 0; j < 32; j++){
            if(val & 0x80000000){
                printf("1");
            }
            else printf("0");
            val = val << 1;
        }
        printf("\n");
    }
}

int main()
{
    int arr[2] = {10,1024};
    print_bits(arr, 2);
    int arr1[2] = {32,1152};
    print_bits(arr1, 2);
    int arr2[2] = {1,138};
    print_bits(arr2, 2);
}