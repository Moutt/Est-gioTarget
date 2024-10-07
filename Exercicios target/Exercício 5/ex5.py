#Usuário informa a palavra que ele deseja inverter
palavra = input("digite uma palavra: ")
tamanho = len(palavra)

#criando pilha
pilha = []

#inserindo valores na pilha
for letra in palavra:
    pilha.append(letra)

#retirando os valores da pilha, seguindo a lógico LIFO, último que entra é o primeiro que sai
print("A palavra invertida fica: ")
for i in palavra:
    print(pilha.pop(), end='')
    