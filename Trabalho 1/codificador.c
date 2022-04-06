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

#define LIBRARY_SIZE 256
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

int encoder(char *file_name)
{
    // Array dos chars e as suas ocorrencias
    int arr_of_occurances[2][LIBRARY_SIZE];

    for(int i = 0; i < 256 ; i++)
    {
        arr_of_occurances[0][i] = i;
    }

    float fmp[LIBRARY_SIZE];
    int n_symbols_by_file = 0;

    // Contar o numero de ocorrencias de cada symbol por ficheiro
    for (int j = 0; j < LIBRARY_SIZE; j++)
    {
        arr_of_occurances[1][j] = count_symbol(file_name, (char)j);
        printf("Tou a contar cada ocorrencia\n");
    }

    // Contar o total de symbols por ficheiro
    for (int k = 0; k < LIBRARY_SIZE; k++)
    {
        n_symbols_by_file += arr_of_occurances[1][k];
        printf("Tou a contar todas a ocorrencias\n");
    }

    printf("Vou começar a ordenar\n");
    for (int x = 0; x < LIBRARY_SIZE - 1; x++)
    {
        for (int y = 0; y < LIBRARY_SIZE - x - 1; y++)
        {
            if (arr_of_occurances[1][y] > arr_of_occurances[1][y + 1])
            {
                int tempN = arr_of_occurances[1][y];
                arr_of_occurances[1][y] = arr_of_occurances[1][y + 1];
                arr_of_occurances[1][y + 1] = tempN;

                int tempChar = arr_of_occurances[0][y];
                arr_of_occurances[0][y] = arr_of_occurances[0][y + 1];
                arr_of_occurances[0][y + 1] = tempChar;
            }
        }
    }
    printf("ORDENEI!\n");

    printf("A Calcular a FMP da cada Symbol\n");

    // Calcular a funçao massa de probabilidade de cada symbol no ficheiro
    for (int f = 0; f < LIBRARY_SIZE; f++)
    {
        fmp[f] = arr_of_occurances[1][f] / n_symbols_by_file;
        printf("%f", fmp[f]);
    }
    printf("Calculei a FMP de cada symbol\n");
    return 0;
}

int main()
{
    printf("Inicio\n");
    // Array de nomes dos ficheiros
    char filename[NUMBER_OF_FILES][FILENAME_SIZE] = {
        "a.txt",
        "alice29.txt",
        "cp.htm",
        "lena.bmp",
        "Person.java",
        "progc.c"};


    printf("Vou entrar do encoder\n");
    int res = encoder(&filename[0][0]);
    printf("%d", res);

    return 0;
}
