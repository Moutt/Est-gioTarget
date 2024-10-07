import dataBase
from dataBase import faturamentos

#Criando variáveis
percentuais = []
soma = 0

#somando todos os valores para saber o percentual total
for dia in faturamentos:
    soma += dia["valor"]
    
#calculando a porcentagem de faturamento de cada estado dividindo o valor de faturamento dele pelo valor de faturamento total
for dia in faturamentos:
    porcentagem = (dia["estado"], (dia["valor"] / soma) * 100)
    percentuais.append(porcentagem)
    print(f'O estado {dia["estado"]} teve um percentual de representação de : {(dia["valor"] / soma) * 100}')
    

