'''

CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS
E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR SHORT())
NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.

'''

lista = []

for c in range(0,5):
    n = int(input('Digite um valor:  '))

    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista... ')

    elif n > lista[-1]:
        lista.append(n)

    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição += 1

print()
print(f'Os valores digitados em ordem foram {lista}')