#include <stdio.h>
#include<stdbool.h>

//função recursiva Fibonacci para verificar se valor esta na sequencia de Fibonacci
bool Fibonacci(int valor, int num1, int num2){
    
    //caso encontre o valor na sequencia ou passe do valor então tem um retorno
    if(valor == num2){
        //retorno para caso encontrar o valor
        return true;
    }
    else if(valor < num2){
        //retorno para caso passar do valor e ele não for encontrado na sequência
        return false;
    }

    num1 = num1 + num2;
    //seguindo para proximo valor na sequência de Fibonacci
    return Fibonacci(valor, num2, num1);
}

int main()
{
    printf("***Verificador de número na sequência de Fibonacci***\n");
    
    //Atribuindo valor que sera Verificado
    int valor;
    bool resposta;
    printf("Digite o valor: ");
    scanf("%d", &valor);
    
    //verificação para valor zero,caso contrario faz a verificação chamando a função recursiva Fibonacci
    if(valor == 0){
        resposta =  true;
    } else{
        resposta = Fibonacci(valor, 0, 1);
    }
    
    
    //Imprimindo na tela caso valor esteja ou não na sequencia de Fibonacci
    if(resposta){
        printf("%d está dentro da sequencia de Fibonacci !!", valor);
    }else{
        printf("%d não está dentro da sequencia de Fibonacci !!", valor);
    }
}