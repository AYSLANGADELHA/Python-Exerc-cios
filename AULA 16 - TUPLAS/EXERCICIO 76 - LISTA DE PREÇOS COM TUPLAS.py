'''

CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS
E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA. NO FINAL, MOSTRE UMA LISTAGEM
DE PREÇOS. ORGANIZANDO OS DADOS EM FORMA TABULAR.

'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25 ,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)

for pos in range (0, len(listagem)): #pos de posição

    if pos % 2 == 0: # para alinhar da listagem os produtos que estiverem na posição par

        print(f'{listagem[pos]:.<30}', end = ' ') # 30 de 30 caracteres 
                                       # . (vários pontos) e < (alinhado para esquerda)

                                       
    else: # alinhar os preços que estão na posição impar
        print(f'R${listagem[pos]:>7.2f}') # alinahdo para direita com 15 posições

print('-' * 40)