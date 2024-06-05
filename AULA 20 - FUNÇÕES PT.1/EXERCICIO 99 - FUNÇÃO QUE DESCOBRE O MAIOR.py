'''

FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(),
QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS. SEU
PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL 
DELES É MAIOR.

'''

from time import sleep
from random import randint

def maior(* núm):
    cont = 0
    maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados')
    
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)

        if cont == 0:
            maior = valor
        
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor analisado foi {maior}')

            

    
    










# Programa Principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()