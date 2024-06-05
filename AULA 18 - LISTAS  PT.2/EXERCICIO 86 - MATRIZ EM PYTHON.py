'''

CRIE UM PROGRAMA QUE CRIE UMA MATRIZ DE DIMENSÃO 3X3
E PREENCHA COM VALORES  LIDOS PELO TECLADO.

NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA.

'''


matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0
maior_valor = 0
soma_coluna = 0




for linha in range(0,3): # pois a linha da matriz são de 0 a 2 
    for coluna in range(0,3): # pois na coluna da matriz é de 0 a 2
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('=-'*30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
        if matriz[linha] [coluna] % 2 == 0: #RESOLUÇÃO ITEM A
            soma_pares = soma_pares + matriz[linha] [coluna]

    print()

# ITEM A) A SOMA DE TODOS VALORES PARES
# ITEM B) A SOMA DOS VALORES DA TERCEIRA COLUNA
# ITEM C) O MAIOR VALOR DA SEGUNDA LINHA

# RESOLUÇÃO ITEM A

print('=-='*35)

for linha in range (0,3): # RESOLUÇÃO ITEM B
    soma_coluna = soma_coluna + matriz[linha] [2]



# RESOLUÇÃO ITEM C
for coluna in range(0,3):
    if coluna == 0:
        maior_valor = matriz [1] [coluna]
    elif matriz [1] [coluna] > maior_valor:
        maior_valor = matriz [1] [coluna]

print(f'A soma dos valores pares {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna} ')
print(f'O maior valor da segunda linha é {maior_valor}')