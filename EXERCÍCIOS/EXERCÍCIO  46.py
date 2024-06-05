'''
FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM
REGRESSIVA PARA ESTOURO DE FOGOS DE ARTIFICIO, INDO DE
10 ATÉ 0, COM UMA PAUSE DE 1 SEGUNDO ENTRE ELES.
'''
from time import sleep
fogos: int(input('Digite o número 1 para estourar os fogos de artifício: '))
print('''CONTAGEM REGRESSIVA
AFASTE-SE ''')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('FOGOS DE ARTIFÍCIO ESTOURADO COM SUCESSO')