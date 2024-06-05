'''

CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES
RESULTADOS EM UM DICIONÁRIO. NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR
TIROU O MAIOR NÚMERO NO DADO.

'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = { 'JOGADOR 1': randint (1,6),
         'JOGADOR 2': randint (1,6),
         'JOGADOR 3': randint (1,6),
         'JOGADOR 4': randint (1,6)}

ranking = {}
print('VALORES SORTEADOS: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado .')
    sleep(1)

ranking = sorted(jogo.items(), key =itemgetter(1), reverse=True ) # 1 significa o valor do randint de jogo
                                                # key=itemgetter serve para ordenar o dicionario
                                                # reverse=True serve para reverter a ordem
print('-=' * 30)
print('==RANKING JOGADORES==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.') #indice é a ordem do jogador
                                            # v[0] qual jogador é
                                            # v[1] quanto tirou no dado em ordem decrescente