'''

CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL.
O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU.
DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL
TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO INCLUINDO TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.

'''

time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    total = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partida.clear()

    for c in range(0,total):
        partida.append(int(input(f'     Quantos gols na partida {c+1} : ')))

    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida) # somar os gols na variavel partida
    time.append(jogador.copy())
    while True: 
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N ')
    if resp in 'N':
        break

print('-=' * 30)
print('cod ', end = '')
for i in jogador.keys():                  #CABEÇALHO
    print(f'{i:>15}', end = '')
print()


print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end = '')
    print()
print('-' * 40)


while True:
    busca = int(input('Mostrar dados de qual jogador?  (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca} !')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ['nome']}: ')
        for i, g in enumerate(time[busca] ['gols'] ):
            print(f'    No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')



'''
APRIMORE O CÓDIGO PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA
DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR.

'''

