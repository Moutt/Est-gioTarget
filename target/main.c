#include <stdio.h>

int main()
{
    //Criando variáveis
    int indice = 13;
    int soma = 0;
    
    //Loop para incrementar na variável soma
    for(int k = 0; k < indice; k++){
        soma += k;
    }
    
    //mostrando resultado da soma
    printf("O resultado para a soma obtido é : %d", soma);
}