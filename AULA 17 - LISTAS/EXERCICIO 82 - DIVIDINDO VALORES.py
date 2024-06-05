'''

CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.
DEPOIS DISSO CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS OS VALORES PARES
E OS VALORES IMPARES DIGITADOS, RESPECTIVAMENTE. AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS
GERADAS.

'''

lista = []
lista_pares = []
lista_impares = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]

    if resp in 'Nn':
        break




for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)

print('=-=' * 30)

print(f'Os números da lista são {lista}')
print(f'Os números pares incluidos na lista são {lista_pares}')
print(f'Os números impares incluidos na lista são {lista_impares}')