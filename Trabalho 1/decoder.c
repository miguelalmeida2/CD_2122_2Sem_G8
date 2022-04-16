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
    char file_name_encoded[64] = "";
    strcat(file_name_encoded, (char *)file_name);
    strcat(file_name_encoded, "_encoded");

    char file_name_decoded[64] = "";
    strcat(file_name_decoded, (char *)file_name);
    strcat(file_name_decoded, "_decoded");

    char modelo[LIBRARY_SIZE];

    FILE *file_read, *file_write;
    file_write = fopen(file_name_decoded, "w");
    file_read = fopen(file_name_encoded, "r");
    char sut = fgetc(file_read);

    // Ler o modelo acaba quando encontro o primeiro caracter repetido
    char *pch;
    for (int i = 0;; i++)
    {
        pch = strchr(modelo, sut);
        if (pch != NULL)
        {
            pch = strchr(pch + 1, sut);
            //modelo[i] = sut;
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

    sut = getc(file_read);
    // printf("%c", sut);
    while (sut != EOF)
    {
        if (sut == '0')
        {
            fputc(modelo[0], file_write);
            printf("%c", modelo[0]);
            sut = getc(file_read);
        }
        else
        {
            // fwrite(bit,1,1,file_encoded);
            int cnt = 0;
            while (sut != '0')
            {
                sut = getc(file_read);
                cnt++;
                // bit = 0x1;
                // fwrite(bit,1,1,file_encoded);
                // bit = 0x0;
            }
            fputc(modelo[cnt], file_write);
            sut = getc(file_read);
            printf("%c", modelo[cnt]);
        }
    }
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
