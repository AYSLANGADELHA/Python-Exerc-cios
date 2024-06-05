#escreva um programa que faça o computador 'pensar'
#em um número inteiro entre 0 e 5 e peça para o usuario
#tentar descobrir qual foi o número escolhido pelo
#computador. O programa deve escrever na tela se o
#usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5) # faz o computador sortear
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei ? ')) #jogador tenta advinhar
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS, você acertou')
else:
    print('Você perdeu, eu pensei no {} e não no {}'.format(computador, jogador))

