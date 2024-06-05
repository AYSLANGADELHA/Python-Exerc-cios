'''
CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS 
E COLOCAR EM UMA TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS
E TAMBÉM INDIQUE O MAIOR E O MENOR VALOR QUE ESTÃO NA TUPLA
'''

from random import randint

menor = 0
maior = 0

números = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10))

print(f'Eu sorteei os valores: {números}')

print(f'O maior valor sorteado foi {max(números)}') # max usado em tuplas (maior valor)
print(f'O menor valor sorteado foi {min(números)}') # min usado em tuplas (menor valor)