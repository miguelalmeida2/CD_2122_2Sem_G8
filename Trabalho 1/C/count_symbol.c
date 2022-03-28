#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

int count_symbol(char *file_name, char symbol)
{
    FILE *file;
    file = fopen(file_name, "r");
    char sut = fgetc(file);
    int cnt = 0;
    while (sut != EOF)
    {
        if (sut == symbol)
        {
            cnt++;
        }
        sut = fgetc(file);
    }
    fclose(file);
    return cnt;
}

int main()
{
    char sut = '1';
    char filename[32] = "exemplo.txt";
    int res = count_symbol(filename, sut);
    printf("Symbol Count = %d\n", res);

    char sut1 = 'b';
    char filename1[32] = "exemplo.txt";
    int res1 = count_symbol(filename1, sut1);
    printf("Symbol Count = %d\n", res1);

    char sut2 = 'D';
    char filename2[32] = "exemplo.txt";
    int res2 = count_symbol(filename2, sut2);
    printf("Symbol Count = %d\n", res2);
}