import dataBase
from dataBase import faturamento

#definindo variaveis
menor = faturamento[0]["valor"]
maior = 0
media = 0
contMaiorMedia = 0

#Loop para verificação de cada valor para buscar menor e mair enquanto soma os valores para obter média
for dia in faturamento:
    if dia["valor"] < menor and dia["valor"] != 0:
        menor = dia["valor"]
    if dia["valor"] > maior:
        maior = dia["valor"]
    media += dia["valor"]
media = media/len(faturamento)

#Contando quantos dias estão com um faturamento maior que a média
for dia in faturamento:
    if dia["valor"] > media:
        contMaiorMedia += 1

   
print(f'O menor faturamento desse mês foi de: {menor}')
print(f'O maior faturamento desse mês foi de: {maior}')
print(f'{contMaiorMedia} dias tiveram o faturamento maior que a média')

