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

    char modelo[256];
    char buffer[1024];

    FILE *file_read, *file_write;
    file_write = fopen(file_name_decoded, "w");
    file_read = fopen(file_name_encoded, "r");
    char sut = fgetc(file_read);
    char curr_char;

    // Ler o modelo acaba quando encontro o primeiro caracter repetido
    char *pch;
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
    int i = 0;
    for (; sut != EOF; i++)
    {
        int j = 0;
        for (;; j++)
        {
            curr_char = sut;
            sut = fgetc(file_read);
            if(sut == NULL || sut == EOF) break;
            if ( (curr_char == '0' && sut == '0') || (curr_char == '1' && sut == '0'))
            {
                fputc(modelo[j], file_write);
                buffer[i] = modelo[j];
                printf("%c",modelo[j]);
                break;
            }
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
