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

    char *modelo[256];
    for (int i = 0; i <= 255; i++)
    {
                modelo[i] = '∆';
    }
    
    FILE *file_read, *file_write;
    file_write = fopen(file_name_decoded,"w");
    file_read  = fopen(file_name_encoded, "r");
    char sut = fgetc(file_read);
    char pch;
    // Ler o modelo acaba quando encontro o primeiro caracter repetido
    for (int i = 0; ; i++)
    {
        pch = (char *)memchr(modelo, sut, strlen(modelo));
        if (pch != NULL)
        {
            printf("%c already read/found!!\n", sut);
            break;
        }
        else
        {
            // printf("%c not found.\n",sut);
            modelo[i] = sut;
            sut = fgetc(file_read);
        }
    }
    // Aqui já tenho modelo vou começar a ler o binário e escrever
    //  num ficheiro o descodificado

    
    //for (size_t i = 0; i < count; i++)
    //{
        /* code */
    //}
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
