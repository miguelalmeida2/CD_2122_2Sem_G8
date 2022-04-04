// Contar os symbols do ficheiro
// Contar a probabilidade de cada symbolo no ficheiro
// Calcular a função FMP de cada symbolo
// Ordenar do mais provavel para o menos provavel
// Ir atribuindo um código binário do mais provável para menos

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <string.h>

#define LIBRARY_SIZE 128
#define NUMBER_OF_FILES 6
#define FILENAME_SIZE 32

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
    // Array de nomes dos ficheiros
    char filename[6][32] = {
        "a.txt",
        "alice29.txt",
        "cp.htm",
        "lena.bmp",
        "Person.java",
        "progc.c"};

    // Array para contar o numero de ocurrencias de symbol por ficheiro
    int arr_of_occurances[6][128];
    int fmp[6][128];

    // Soma das ocurrencias dos symbolos por ficheiro
    int n_symbols_by_file[6];

    // Percorrer os ficheiros
    for (int i = 0; i < 6; i++)
    {
        // Contar o numero de ocorrencias de cada symbol por ficheiro
        for (int j = 0; j < 128; j++)
        {
            arr_of_occurances[i][j] = count_symbol(&filename[i][0], (char)j);
        }
        // Contar o total de symbols por ficheiro
        for (int k = 0; k < 128; k++)
        {
            n_symbols_by_file[i] += arr_of_occurances[i][k];
        }
        // Calcular a funçao massa de probabilidade de cada symbol no ficheiro
        for (int f = 0; f < 128; f++)
        {
            fmp[i][f] = arr_of_occurances[i][f] / n_symbols_by_file[i];
        }
        
    }
    printf("%d", *arr_of_occurances[0]);
}