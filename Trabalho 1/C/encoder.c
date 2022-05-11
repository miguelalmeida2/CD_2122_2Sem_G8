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

unsigned char charArrayToByte(char *buffer)
{
    unsigned char binaryBuffer = 0;
    int i = 0;

    while (1)
    {
        if (buffer[i] == '0' || buffer[i] == '1')
        {
            break;
        }
        i++;
    }

    int size = i + 7;
    for (; i <= size; i++)
    {
        if (buffer[i] == '0')
        {
            if (i != size)
            {
                binaryBuffer = binaryBuffer << 1;
            }
        }
        else
        {
            binaryBuffer++;
            if (i != size)
            {
                binaryBuffer = binaryBuffer << 1;
            }
        }
    }
    return binaryBuffer;
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
    unsigned char *modelo[256];

    for (int i = 0; i < 256; i++)
    {
        arr_of_occurances[0][i] = i;
        arr_of_occurances[1][i] = 0;
    }

    // Contar o numero de ocorrencias de cada symbol por ficheiro
    FILE *file_read;
    file_read = fopen(file_name, "r");
    unsigned char sut = fgetc(file_read);
    while (!feof(file_read))
    {
        arr_of_occurances[1][sut]++;
        sut = fgetc(file_read);
    }
    fclose(file_read);

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
    // printf("\n");
    // printf("Soma de symbols = %d e nº de simbolos usados foi = %d\n", n_symbols_by_file, n_symbols_used_by_file);
    // printf("Total de FMP = %f\n", fmp_sum);

    // for para a escrita em modo semi-adaptativo no ficheiro saída
    FILE *file_encoded, *file;
    file = fopen(file_name, "r");
    file_encoded = fopen(file_name_encoded, "w+b");

    // Criar a string modelo para colocar no ficheiro encoded
    int f = 255;
    for (; fmp[f] != 0; f--)
    {
        modelo[f] = arr_of_occurances[0][f];
        printf("%c", modelo[f]);
        fputc(modelo[f], file_encoded);
    }
    fputc(modelo[++f], file_encoded);
    printf("\n");

    //--------------------------------------------------------

    sut = getc(file);
    unsigned char bufferBinary = 0x0;
    char buffer[10] = " ";
    unsigned char bitCounter = 0;
    while (!feof(file))
    {
        if (arr_of_occurances[0][255] == sut)
        {
            // bit = '0';
            // printf("0");
            strcat(buffer, "0");
            bitCounter++;
            if (bitCounter != 0)
            {
                if (bitCounter % 8 == 0)
                {
                    bufferBinary = charArrayToByte(&buffer);
                    fwrite(&bufferBinary, 1, 1, file_encoded);
                    memset(buffer, '\0', sizeof buffer);
                    bitCounter = 0;
                }
            }
            // printf("%c", sut);
            sut = getc(file);
        }
        else
        {
            for (int c = 255; arr_of_occurances[0][c] != sut; c--)
            {
                //    bit = '1';
                // printf("1");
                strcat(buffer, "1");
                bitCounter++;
                if (bitCounter != 0)
                {
                    if (bitCounter % 8 == 0)
                    {
                        bufferBinary = charArrayToByte(&buffer);
                        fwrite(&bufferBinary, 1, 1, file_encoded);
                        memset(buffer, '\0', sizeof buffer);
                        bitCounter = 0;
                    }
                }
            }
            // bit = '0';
            strcat(buffer, "0");
            bitCounter++;
            if (bitCounter != 0)
            {
                if ((bitCounter % 8) == 0)
                {
                    bufferBinary = charArrayToByte(&buffer);
                    fwrite(&bufferBinary, 1, 1, file_encoded);
                    memset(buffer, '\0', sizeof buffer);
                    bitCounter = 0;
                }
            }
            //  printf("%c", sut);
            sut = getc(file);
        }
    }
    while (bitCounter < 7)
    {
        // printf("1");
        strcat(buffer, "1");
        bitCounter++;
    }
    // printf("1");
    strcat(buffer, "1");
    bufferBinary = charArrayToByte(&buffer);
    fwrite(&bufferBinary, 1, 1, file_encoded);
    memset(buffer, '\0', sizeof buffer);

    printf("\n");

    fclose(file_encoded);
    fclose(file);
}

int main()
{
    // Array de nomes dos ficheiros
    char filename[NUMBER_OF_FILES][FILENAME_SIZE] = {
        "../CD_TestFiles/a.txt",
        "../CD_TestFiles/alice29.txt",
        "../CD_TestFiles/cp.htm",
        "../CD_TestFiles/lena.bmp",
        "../CD_TestFiles/Person.java",
        "../CD_TestFiles/progc.c"};

    encoder(&filename[0][0]);
    encoder(&filename[1][0]);
    encoder(&filename[2][0]);
    encoder(&filename[3][0]);
    encoder(&filename[4][0]);
    encoder(&filename[5][0]);
}
