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
#define UNARY_MAX_SIZE 64

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

void encoder(const char *file_name)
{
    char file_name_encoded[64] = "";
    strcat(file_name_encoded, file_name);
    strcat(file_name_encoded, "_encoded");

    // Array dos chars e as suas ocorrencias
    unsigned int arr_of_occurances[2][LIBRARY_SIZE];
    float fmp[LIBRARY_SIZE];
    float fmp_sum = 0;
    unsigned int n_symbols_by_file = 0;
    unsigned int n_symbols_used_by_file = 0;
    char *modelo[256];

    for (int i = 0; i < 256; i++)
    {
        arr_of_occurances[0][i] = i;
    }

    // Contar o numero de ocorrencias de cada symbol por ficheiro
    for (int j = 0; j < LIBRARY_SIZE; j++)
    {
        arr_of_occurances[1][j] = count_symbol((char *)file_name, (char)j);
    }

    // Contar o total de symbols por ficheiro
    for (int k = 0; k < LIBRARY_SIZE; k++)
    {
        n_symbols_by_file += arr_of_occurances[1][k];
        if (arr_of_occurances[1][k] != 0)
        {
            n_symbols_used_by_file++;
        }
    }

    // Ordenar os symbols pela quantidade de ocurrencias
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

    // Calcular a funçao massa de probabilidade de cada symbol no ficheiro
    for (int f = 0; f < LIBRARY_SIZE; f++)
    {
        fmp[f] = arr_of_occurances[1][f] / (float)n_symbols_by_file;
        fmp_sum += fmp[f];
        /*
        if (fmp[f] != 0)
        {
            printf("%c -> %f;\n", (char)arr_of_occurances[0][f], fmp[f]);
        }
        */
    }
    printf("\n");
    printf("Soma de symbols = %d e nº de simbolos usados foi = %d\n", n_symbols_by_file, n_symbols_used_by_file);
    printf("Total de FMP = %f\n", fmp_sum);

    // for para a escrita em modo semi-adaptativo no ficheiro saída
    FILE *file_encoded, *file;
    file = fopen(file_name, "r");
    file_encoded = fopen(file_name_encoded, "w+");

    // Criar a string modelo para colocar no ficheiro encoded
    printf("--------------------------------------\n");
    printf("\t    MODELO!!\n");
    printf("\n");
    int f = 255;
    for (; fmp[f] != 0; f--)
    {
        modelo[f] = (char)arr_of_occurances[0][f];
        printf("%c", (char)modelo[f]);
        fputc(modelo[f], file_encoded);
    }
    fputc(modelo[f+1], file_encoded);
    printf("\n");
    printf("--------------------------------------\n\t    Texto a Escrever:\n");
    printf("\n");
    char sut = getc(file);
    //printf("%c", sut);
    char bit = '0';
    while (sut != EOF)
    {
        if (arr_of_occurances[0][255] == sut)
        {
            bit = '0';
            fputc(bit, file_encoded);
            printf("%c", sut);
            sut = getc(file);
        }
        else
        {
            // fwrite(bit,1,1,file_encoded);
            for (int c = 255; arr_of_occurances[0][c] != sut; c--)
            {
                bit = '1';
                fputc(bit, file_encoded);
                // bit = 0x1;
                // fwrite(bit,1,1,file_encoded);
                // bit = 0x0;
            }
            bit = '0';
            fputc(bit, file_encoded);
            sut = getc(file);
            printf("%c", sut);
        }
    }

    printf("\n");
    printf("--------------------------------------\n");
}

int main()
{
    // Array de nomes dos ficheiros
    char filename[NUMBER_OF_FILES][FILENAME_SIZE] = {
        "a.txt",
        "alice29.txt",
        "cp.htm",
        "lena.bmp",
        "Person.java",
        "progc.c"};

    encoder(&filename[0][0]);
}
