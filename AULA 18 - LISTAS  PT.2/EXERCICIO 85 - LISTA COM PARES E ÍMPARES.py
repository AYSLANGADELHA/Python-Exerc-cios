'''

CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR 7 VALORES NUMÉRICOS
E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES
IMPARES E PARES. NO FINAL, MOSTRE OS VALORES MARES E ÍMPARES EM ORDEM CRESCENTE.

'''

núm = [[], []] #1ª lista dos pares e 2ª lista dos ímpares
valor = 0

for c in range(1,8):
    valor = int(input(f'Digite {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)

print('-=' * 30)
núm[0].sort #organizar o indice 0(que é uma lista) da lista núm
núm[1].sort #organizar o indice 1(que é uma lista) da lista núm
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímpares digitados foram: {núm[1]}')




