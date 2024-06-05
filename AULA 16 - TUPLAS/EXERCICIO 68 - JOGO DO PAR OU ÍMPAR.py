'''
FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO
O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO
'''

from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
       tipo = str(input('Par ou Ímpar ? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} .')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
     if total % 2 == 1:
          print('Você VENCEU')
          v = v + 1
     else:
          print('Você PERDEU!')
          break
     print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')



