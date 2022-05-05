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

void decoder(const char *file_name)
{
    unsigned char file_name_encoded[64] = "";
    strcat(file_name_encoded, (char *)file_name);
    strcat(file_name_encoded, "_encoded");

    unsigned char file_name_decoded[64] = "";
    strcat(file_name_decoded, (char *)file_name);
    strcat(file_name_decoded, "_decoded");

    unsigned char modelo[LIBRARY_SIZE];

    FILE *file_read, *file_write;
    file_write = fopen(file_name_decoded, "w");
    file_read = fopen(file_name_encoded, "rb");
    unsigned char sut = fgetc(file_read);
    unsigned char buffer = 0;

    // Ler o modelo acaba quando encontro o primeiro caracter repetido
    unsigned char *pch;
    for (int i = 0;; i++)
    {
        pch = strchr(modelo, sut);
        if (pch != NULL)
        {
            pch = strchr(pch + 1, sut);
            break;
        }
        else
        {
            modelo[i] = sut;
            sut = fgetc(file_read);
        }
    }

    // Aqui já tenho modelo vou começar a ler o binário e escrever
    //  num ficheiro o descodificado

    buffer = fgetc(file_read);
    unsigned char bit = 128;
    unsigned int bitCounter = 0;
    while (!feof(file_read))
    {
        if ((buffer & bit) == 0)
        {
            bitCounter++;
            if (bitCounter != 0)
            {
                if (bitCounter % 8 == 0)
                {
                    buffer = fgetc(file_read);
                    bit = 128;
                }
            }
            fputc(modelo[0], file_write);
            printf("%c", modelo[0]);
            bit = bit >> 1;
        }
        else
        {
            int cnt = 0;
            while ((buffer & bit) > 0)
            {
                bitCounter++;
                if (bitCounter != 0)
                {
                    if (bitCounter % 8 == 0)
                    {
                        buffer = fgetc(file_read);
                        bit = 128;
                    }
                }
                cnt++;
                bit = bit >> 1;
            }
            fputc(modelo[cnt], file_write);
            printf("%c", modelo[cnt]);
        }
    }
    fclose(file_read);
    fclose(file_write);
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

    decoder(&filename[0][0]);
}
